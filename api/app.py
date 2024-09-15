from flask import Flask, request, jsonify
import redis
import grpc
import dns_pb2
import dns_pb2_grpc

app = Flask(__name__)

# Conexiones a Redis
redis_part1 = redis.StrictRedis(host='redis-part1', port=6379, decode_responses=True)
redis_part2 = redis.StrictRedis(host='redis-part2', port=6379, decode_responses=True)

def get_redis_partition(domain_name):
    # Implementación de partición simple por hash
    return redis_part1 if hash(domain_name) % 2 == 0 else redis_part2

def resolve_dns(domain_name):
    # Conexión con el servidor gRPC
    with grpc.insecure_channel('grpc-server:50051') as channel:
        stub = dns_pb2_grpc.DNSResolverStub(channel)
        response = stub.Resolve(dns_pb2.DomainRequest(domain_name=domain_name))
        return response.ip_address

@app.route('/resolve', methods=['POST'])
def resolve_domain():
    domain_name = request.json['domain']
    partition = get_redis_partition(domain_name)
    cached_ip = partition.get(domain_name)

    if cached_ip:
        return jsonify({'status': 'HIT', 'ip': cached_ip})
    else:
        ip = resolve_dns(domain_name)
        partition.setex(domain_name, 360, ip)  # Guardar con TTL de 1 hora
        return jsonify({'status': 'MISS', 'ip': ip})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
