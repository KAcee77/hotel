from app.models.hotel import CreateRoom, Room
from app.services.hotel import RoomActions
from fastapi import APIRouter, Depends

from ..utils import RoleChecker

router = APIRouter(
    prefix='/hotel',
    tags=['hotel'],
)

allow_roles = RoleChecker(['admin'])

# @app.post('/rooms', response_model=Room, dependencies=[Depends(allow_roles)])
@router.post('/rooms', response_model=Room)
async def create(room: CreateRoom, room_actions: RoomActions = Depends()):
    return await room_actions.create(room)

# @router.post('/bookings')
# async def create_booking(*, session: AsyncSession = Depends(get_session), booking: Booking):
#     booking = await create_obj(session, booking)
#     return {'Booking number': booking.id}
