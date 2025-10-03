from manim import *

class Algorithm_merge(Scene):
    def construct(self):

        data = [2, 4, 5, 1, 3, 9, 6, 8, 7]  # raw unsorted data

        plane = NumberPlane(x_range=[-5, 5], y_range=[-4, 4], x_length=10, y_length=8)  # used to set location
        colors = [RED, GREEN, BLUE, YELLOW, PURPLE, ORANGE, PINK, TEAL, MAROON] # different colors for each number

        items = VGroup()  # items consists mobjects correspond to integers in data
        for i in range(len(data)):
            number = Integer(data[i]).set(height=0.3)
            box = SurroundingRectangle(number, color=colors[i], fill_color=colors[i], fill_opacity=0.3, buff=0.2)
            item = VGroup(box, number).move_to(plane.c2p(-(4 - i)/1.5, 3))
            items.add(item)

        self.play(Create(items), run_time=1.5)
        self.wait(0.5)

        def merge_sort(items):
            if len(items) == 1:
                return items
            else:
                # split the numbers into two groups and separate them
                half_length = len(items) // 2
                left_items = items[:half_length].copy()
                right_items = items[half_length:].copy()
                self.play(left_items.animate.shift(DOWN*1.2 + LEFT*len(left_items)/4), run_time=0.5)
                self.play(right_items.animate.shift(DOWN*1.2 + RIGHT*len(right_items)/4), run_time=0.5)
                merge(merge_sort(left_items), merge_sort(right_items), items)
                return items

        def merge(left_items, right_items, items):
            a = 0
            b = 0

            self.play(FadeOut(items), run_time=0.5)
            while a < len(left_items) and b < len(right_items):
                # since item is a VGroup(box, integer_object), we use items[index][1].get_value()
                if left_items[a][1].get_value() <= right_items[b][1].get_value():
                    self.play(left_items[a].animate.move_to(items[a + b].get_center()), run_time=0.5)
                    items[a + b] = left_items[a]
                    a += 1
                else:
                    self.play(right_items[b].animate.move_to(items[a + b].get_center()), run_time=0.5)
                    items[a + b] = right_items[b]
                    b += 1

            if a == len(left_items):
                anims = []  # store the animations in a list and play them together
                while b < len(right_items):
                    anims.append(right_items[b].animate.move_to(items[a + b].get_center()))
                    items[a + b] = right_items[b]
                    b += 1
                self.play(*anims, run_time=0.5)
            else:
                anims = []
                while a < len(left_items):
                    anims.append(left_items[a].animate.move_to(items[a + b].get_center()))
                    items[a + b] = left_items[a]
                    a += 1
                self.play(*anims, run_time=0.5)

        merge_sort(items)
        self.wait(0.5)
