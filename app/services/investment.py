from datetime import datetime
from typing import Union

from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.charity_project import charity_project_crud
from app.crud.donation import donation_crude
from app.models import CharityProject, Donation


async def investing(
    source: Union[CharityProject, Donation],
    session: AsyncSession,
) -> Union[CharityProject, Donation]:
    if source.invested_amount is None:
        source.invested_amount = 0
    crud = donation_crude if isinstance(
        source, CharityProject
    ) else charity_project_crud
    for target in await crud.get_not_fully_invested(session):
        session.add(target)
        allocated_amount = (
            (target.full_amount - target.invested_amount)
            if (source.full_amount - source.invested_amount) >
               (target.full_amount - target.invested_amount) else
            (source.full_amount - source.invested_amount)
        )
        for obj in (target, source):
            obj.invested_amount += allocated_amount
            if obj.invested_amount == obj.full_amount:
                obj.fully_invested, obj.close_date = True, datetime.now()
        if source.fully_invested:
            break
    return source
