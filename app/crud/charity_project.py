from typing import Optional

from sqlalchemy import extract, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.charity_project import CharityProject


class CRUDCharityProject(CRUDBase):

    async def get_project_id_by_name(
            self,
            project_name: str,
            session: AsyncSession,
    ) -> Optional[int]:
        db_project_id = await session.execute(
            select(CharityProject.id).where(
                CharityProject.name == project_name
            )
        )
        db_project_id = db_project_id.scalars().first()
        return db_project_id

    def extract_time(self, time_unit):
        collection_time = (extract(time_unit, CharityProject.close_date) -
                           extract(time_unit, CharityProject.create_date))
        return collection_time

    async def get_projects_by_completion_rate(self, session: AsyncSession):
        charity_projects = await session.execute(
            select(CharityProject).where(
                CharityProject.fully_invested
            ).order_by(
                self.extract_time('year'),
                self.extract_time('month'),
                self.extract_time('day'),
            )
        )
        charity_projects = charity_projects.scalars().all()
        return charity_projects


charity_project_crud = CRUDCharityProject(CharityProject)
