import builtins
from _typeshed import Incomplete

import MySQLdb._exceptions

version_info: tuple[Incomplete, ...]

class DataError(MySQLdb._exceptions.DatabaseError): ...
class DatabaseError(MySQLdb._exceptions.Error): ...
class Error(MySQLdb._exceptions.MySQLError): ...
class IntegrityError(MySQLdb._exceptions.DatabaseError): ...
class InterfaceError(MySQLdb._exceptions.Error): ...
class InternalError(MySQLdb._exceptions.DatabaseError): ...
class MySQLError(Exception): ...
class NotSupportedError(MySQLdb._exceptions.DatabaseError): ...
class OperationalError(MySQLdb._exceptions.DatabaseError): ...
class ProgrammingError(MySQLdb._exceptions.DatabaseError): ...
class Warning(builtins.Warning, MySQLdb._exceptions.MySQLError): ...

class connection:
    client_flag: Incomplete
    converter: Incomplete
    open: Incomplete
    port: Incomplete
    server_capabilities: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def _get_native_connection(self, *args, **kwargs): ...
    def affected_rows(self, *args, **kwargs): ...
    def autocommit(self, on): ...
    def change_user(self, *args, **kwargs): ...
    def character_set_name(self, *args, **kwargs): ...
    def close(self, *args, **kwargs): ...
    def commit(self, *args, **kwargs): ...
    def dump_debug_info(self, *args, **kwargs): ...
    def errno(self, *args, **kwargs): ...
    def error(self, *args, **kwargs): ...
    def escape(self, obj, dict): ...
    def escape_string(self, s): ...
    def field_count(self, *args, **kwargs): ...
    def fileno(self, *args, **kwargs): ...
    def get_autocommit(self, *args, **kwargs): ...
    def get_character_set_info(self, *args, **kwargs): ...
    def get_host_info(self, *args, **kwargs): ...
    def get_proto_info(self, *args, **kwargs): ...
    def get_server_info(self, *args, **kwargs): ...
    def info(self, *args, **kwargs): ...
    def insert_id(self, *args, **kwargs): ...
    def kill(self, *args, **kwargs): ...
    def next_result(self): ...
    def ping(self): ...
    def query(self, query): ...
    def read_query_result(self, *args, **kwargs): ...
    def rollback(self, *args, **kwargs): ...
    def select_db(self, *args, **kwargs): ...
    def send_query(self, *args, **kwargs): ...
    def set_character_set(self, charset: str) -> None: ...
    def set_server_option(self, option): ...
    def shutdown(self, *args, **kwargs): ...
    def sqlstate(self, *args, **kwargs): ...
    def stat(self, *args, **kwargs): ...
    def store_result(self, *args, **kwargs): ...
    def string_literal(self, obj): ...
    def thread_id(self, *args, **kwargs): ...
    def use_result(self, *args, **kwargs): ...
    def discard_result(self) -> None: ...
    def warning_count(self, *args, **kwargs): ...
    def __delattr__(self, name: str, /) -> None: ...
    def __setattr__(self, name: str, value, /) -> None: ...

class result:
    converter: Incomplete
    has_next: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def data_seek(self, n): ...
    def describe(self, *args, **kwargs): ...
    def fetch_row(self, *args, **kwargs): ...
    def discard(self) -> None: ...
    def field_flags(self, *args, **kwargs): ...
    def num_fields(self, *args, **kwargs): ...
    def num_rows(self, *args, **kwargs): ...
    def __delattr__(self, name: str, /) -> None: ...
    def __setattr__(self, name: str, value, /) -> None: ...

def connect(*args, **kwargs): ...
def debug(*args, **kwargs): ...
def escape(obj, dict): ...
def escape_string(s): ...
def get_client_info(): ...
def string_literal(obj): ...
