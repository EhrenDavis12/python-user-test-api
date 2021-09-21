from rest_framework import views
from rest_framework.response import Response
from random import randrange

player_ids = ["SunnyBunny#123", "TripleKill360", "HopPocket96", "WulfGang"]
characters = ["Nami", "Ash", "VoileBare", "Leona"]
method = ["Sun Blast", "Watter Bullet", "Arrow volley", "Table Flip"]


class CombatActionView(views.APIView):

    @staticmethod
    def get(request):
        if randrange(0, 99) > 90:
            return Response(
                {
                    "status": "failed",
                    "reason": "Failed to reach Overwatch server for kill feed",
                    "payload": []
                }
            )

        if randrange(0, 99) > 90:
            return Response({
                "error": 500,
                "message": "Cthulu ate my JSON response"
            }, 500)

        return Response(
            {
                "status": "successful",
                "reason": "OK",
                "payload": [
                    {
                        "source_player_id": player_ids[randrange(0, 3)],
                        "source_character": characters[randrange(0, 3)],
                        "target_player_id": player_ids[randrange(0, 3)],
                        "target_character": characters[randrange(0, 3)],
                        "method": method[randrange(0, 3)],
                        "damage": randrange(1, 100),
                    }
                ]
            }
        )
