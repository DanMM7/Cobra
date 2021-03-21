import tkinter as tk
from PIL import Image, ImageTk

MOVE_INCREMENT = 20


class Snake(tk.Canvas):
    def __init__(self):
        super().__init__(width=600, height=620, background="brown", highlightthickness=0)

        self.snake_positions = [(100, 100), (80, 100), (60, 100)]
        self.food_position = (200, 100)

        self.load_assets()
        self.create_objects()

        self.after(75, self.perform_actions)

    def load_assets(self):
        try:
            self.snake_body_image = Image.open("./assets/snake.jpg")
            self.snake_body = ImageTk.PhotoImage(self.snake_body_image)
            self.score = 0

            self.food_image = Image.open("./assets/food.jpg")
            self.food = ImageTk.PhotoImage(self.food_image)
        except IOError as error:
            print(error)
            root.destroy()

    def create_objects(self):
        self.create_text(
            45, 12, text=f"Score {self.score}", tag="score", fill="#000", font=("TkDefaultFont", 14)
        )
        for x_position, y_position in self.snake_positions:
            self.create_image(x_position, y_position, image=self.snake_body, tag="snake")

        self.create_image(*self.food_position, image=self.food, tag="food")
        self.create_rectangle(7, 27, 593, 613, outline="#000")

    def move_snake(self):
        head_x_position, head_y_position = self.snake_positions[0]
        new_head_position = (head_x_position + MOVE_INCREMENT, head_y_position)

        self.snake_positions = [new_head_position] + self.snake_positions[:-1]

        for segment, position in zip(self.find_withtag("snake"), self.snake_positions):
            self.coords(segment, position)

    def perform_actions(self):
        self.move_snake()
        self.after(75, self.perform_actions)

root = tk.Tk()
root.title("Cobra")
root.resizable(False, False)

board = Snake()
board.pack()

root.mainloop()


