# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: health.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0chealth.proto\x12\x06health\"\x10\n\x0eHealthCheckDto\"%\n\x13HealthCheckResponse\x12\x0e\n\x06status\x18\x01 \x01(\t2U\n\rHealthService\x12\x44\n\x0b\x43heckHealth\x12\x16.health.HealthCheckDto\x1a\x1b.health.HealthCheckResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'health_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_HEALTHCHECKDTO']._serialized_start=24
  _globals['_HEALTHCHECKDTO']._serialized_end=40
  _globals['_HEALTHCHECKRESPONSE']._serialized_start=42
  _globals['_HEALTHCHECKRESPONSE']._serialized_end=79
  _globals['_HEALTHSERVICE']._serialized_start=81
  _globals['_HEALTHSERVICE']._serialized_end=166
# @@protoc_insertion_point(module_scope)
