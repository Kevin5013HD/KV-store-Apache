#
# Autogenerated by Thrift Compiler (0.9.3)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#

require 'thrift'

class KVMessage
  include ::Thrift::Struct, ::Thrift::Struct_Union
  VALUE = 1

  FIELDS = {
    VALUE => {:type => ::Thrift::Types::MAP, :name => 'value', :key => {:type => ::Thrift::Types::STRING}, :value => {:type => ::Thrift::Types::STRING}}
  }

  def struct_fields; FIELDS; end

  def validate
    raise ::Thrift::ProtocolException.new(::Thrift::ProtocolException::UNKNOWN, 'Required field value is unset!') unless @value
  end

  ::Thrift::Struct.generate_accessors self
end

class KVException < ::Thrift::Exception
  include ::Thrift::Struct, ::Thrift::Struct_Union
  def initialize(message=nil)
    super()
    self.why = message
  end

  def message; why end

  WHY = 1

  FIELDS = {
    WHY => {:type => ::Thrift::Types::STRING, :name => 'why'}
  }

  def struct_fields; FIELDS; end

  def validate
  end

  ::Thrift::Struct.generate_accessors self
end

class KVCollection
  include ::Thrift::Struct, ::Thrift::Struct_Union
  ELEMENTS = 1

  FIELDS = {
    ELEMENTS => {:type => ::Thrift::Types::LIST, :name => 'elements', :element => {:type => ::Thrift::Types::STRUCT, :class => ::KVMessage}}
  }

  def struct_fields; FIELDS; end

  def validate
  end

  ::Thrift::Struct.generate_accessors self
end

