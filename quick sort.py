from manim import *

class Algorithm_quick(Scene):
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

        def quick_sort(items):
            if len(items) <= 1:
                return items
            
            pivot = items[-1].copy()
            p = pivot[1].get_value()

            left_items = VGroup(*[x for x in items[:-1] if x[1].get_value() < p]).copy()
            right_items = VGroup(*[x for x in items[:-1] if x[1].get_value() >= p]).copy()
            left, right = len(left_items), len(right_items)

            self.play(pivot.animate.move_to(items[left].get_center() + DOWN*1.2), run_time=0.5)

            anims = []
            for i in range(left):
                anims.append(left_items[i].animate.move_to(pivot.get_center() + LEFT*(left + 1)/1.5 + RIGHT*i/1.5))
            if anims:
                self.play(*anims, run_time=0.5)

            anims = []
            for i in range(right):
                anims.append(right_items[i].animate.move_to(pivot.get_center() + RIGHT*(right + 1)/1.5 + LEFT*(right - i - 1)/1.5))
            if anims:
                self.play(*anims, run_time=0.5)

            self.wait(0.5)
            left_items_sorted = quick_sort(left_items)
            right_items_sorted = quick_sort(right_items)

            self.play(FadeOut(items), run_time=0.5)
            self.play(left_items_sorted.animate.shift(UP*1.2 + RIGHT/1.5), 
                      pivot.animate.shift(UP*1.2), 
                      right_items_sorted.animate.shift(UP*1.2 + LEFT/1.5), run_time=0.5)
            self.wait(0.5)
            
            return left_items_sorted + VGroup(pivot) + right_items_sorted
        
        quick_sort(items)