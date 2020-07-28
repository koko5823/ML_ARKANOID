"""
The template of the main script of the machine learning process
"""

class MLPlay:
    def __init__(self):
        """
        Constructor
        """
        self.ball_served = False

    def update(self, scene_info):
        """
        Generate the command according to the received `scene_info`.
        """
        # Make the caller to invoke `reset()` for the next round.
        if (scene_info["status"] == "GAME_OVER" or
            scene_info["status"] == "GAME_PASS"):
            return "RESET"
        
        this_ball_x = scene_info["ball"][0]#get ball data
        platform_x = scene_info["platform"][0]+20

        if not self.ball_served:
            self.ball_served = True
            command = "SERVE_TO_LEFT"
        else:
            if platform_x > 150 :
                command = "MOVE_LEFT"
            elif platform_x < 50:
                command = "MOVE_RIGHT"
            elif this_ball_x > platform_x: #right is bigger
                command = "MOVE_RIGHT"
            elif this_ball_x < platform_x: 
                command = "MOVE_LEFT"
            elif this_ball_x == platform_x:
                command = "NONE"
        return command

    def reset(self):
        """
        Reset the status
        """
        self.ball_served = False
