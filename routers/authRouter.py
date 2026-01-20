from fastapi import APIRouter
from fastapi.params import Depends

from authController import authController
router = APIRouter()
from dependencies import proverka_token
auth_controller = authController()

router.add_api_route("/login",
    auth_controller.login,
    methods=["POST"])
router.add_api_route("/registration",
    auth_controller.registration,
    methods=["POST"])
router.add_api_route("/",
    auth_controller.getAll,
    dependencies=[Depends(proverka_token)],
    methods=["GET"])