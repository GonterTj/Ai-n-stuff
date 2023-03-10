from typing import Any

from django.db.backends.mysql.schema import DatabaseSchemaEditor as DatabaseSchemaEditor

logger: Any

class MySQLGISSchemaEditor(DatabaseSchemaEditor):
    sql_add_spatial_index: str = ...
    sql_drop_spatial_index: str = ...
    geometry_sql: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def skip_default(self, field: Any) -> Any: ...
    def column_sql(
        self, model: Any, field: Any, include_default: bool = ...
    ) -> Any: ...
    def create_model(self, model: Any) -> None: ...
    def add_field(self, model: Any, field: Any) -> None: ...
    def remove_field(self, model: Any, field: Any) -> None: ...
    def create_spatial_indexes(self) -> None: ...
