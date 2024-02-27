from typing import Annotated

from fastapi import APIRouter, Depends

from ..agent import Prompt, Scribe

router = APIRouter(
    prefix='/scribe'
)


@router.post('/ask')
async def ask(prompt: Prompt, scribe: Annotated[Scribe, Depends()]):
    return await scribe.ask(prompt.prompt)
