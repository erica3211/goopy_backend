from math import ceil
from typing import TypeVar, Generic
from sqlalchemy.orm import Session

ModelType = TypeVar("ModelType")


class BaseService(Generic[ModelType]):
    model: type[ModelType] | None = None

    def __init__(self, db: Session):
        self.db = db

    def paginate(self, query, page: int, size: int):
        total = query.count()

        items = (
            query
            .offset((page - 1) * size)
            .limit(size)
            .all()
        )

        total_pages = ceil(total / size) if total > 0 else 0

        return {
            "items": items,
            "page": page,
            "size": size,
            "total": total,
            "total_pages": total_pages,
        }
    