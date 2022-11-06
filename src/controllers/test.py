"""Router for test.

- Author: Minki Lee
- Email: minki@naver.com
"""
from fastapi import APIRouter

router = APIRouter(prefix="/test")

@router.get("/getTest", status_code=200)
def export_coco(
    x: int = None, y: int = None, center: int = None
) -> str:
    """Get coordinates."""
    print(x, y, center)

    # 정상 리턴
    return "OK"