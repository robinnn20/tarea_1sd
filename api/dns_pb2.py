# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: dns.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'dns.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tdns.proto\"$\n\rDomainRequest\x12\x13\n\x0b\x64omain_name\x18\x01 \x01(\t\"!\n\x0b\x44NSResponse\x12\x12\n\nip_address\x18\x01 \x01(\t26\n\x0b\x44NSResolver\x12\'\n\x07Resolve\x12\x0e.DomainRequest\x1a\x0c.DNSResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dns_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_DOMAINREQUEST']._serialized_start=13
  _globals['_DOMAINREQUEST']._serialized_end=49
  _globals['_DNSRESPONSE']._serialized_start=51
  _globals['_DNSRESPONSE']._serialized_end=84
  _globals['_DNSRESOLVER']._serialized_start=86
  _globals['_DNSRESOLVER']._serialized_end=140
# @@protoc_insertion_point(module_scope)
