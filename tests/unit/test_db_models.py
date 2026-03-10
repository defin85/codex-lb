from __future__ import annotations

from sqlalchemy import Enum as SqlEnum

from app.db.models import Account, AccountStatus, ApiKeyLimit, LimitType, LimitWindow


def test_sqlalchemy_enums_use_string_values() -> None:
    account_status = Account.__table__.c.status.type
    limit_type = ApiKeyLimit.__table__.c.limit_type.type
    limit_window = ApiKeyLimit.__table__.c.limit_window.type

    assert isinstance(account_status, SqlEnum)
    assert isinstance(limit_type, SqlEnum)
    assert isinstance(limit_window, SqlEnum)

    assert account_status.enums == [status.value for status in AccountStatus]
    assert limit_type.enums == [value.value for value in LimitType]
    assert limit_window.enums == [value.value for value in LimitWindow]
