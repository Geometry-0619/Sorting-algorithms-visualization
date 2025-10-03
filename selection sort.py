from manim import *

class Algorithm_selection(Scene):
    def construct(self):

        data = [2, 4, 5, 1, 3, 9, 6, 8, 7]  # raw unsorted data

        plane = NumberPlane(x_range=[-5, 5], y_range=[-4, 4], x_length=10, y_length=8)  # used to set location
        colors = [RED, GREEN, BLUE, YELLOW, PURPLE, ORANGE, PINK, TEAL, MAROON] # different colors for each number

        items = VGroup()  # items consists mobjects correspond to integers in data
        for i in range(len(data)):
            number = Integer(data[i]).set(height=0.7)
            box = SurroundingRectangle(number, color=colors[i], fill_color=colors[i], fill_opacity=0.3, buff=0.2)
            item = VGroup(box, number).move_to(plane.c2p(-4 + i, -0.4))
            items.add(item)

        comparison_count = 0  

        text2 = Tex("Comparison count: ")
        num2 = always_redraw(lambda: Integer().set_value(comparison_count).next_to(text2, RIGHT, buff=0.3))
        text_group2 = VGroup(text2, num2).next_to(items, UP, buff=1)

        arrow_text1 = MathTex(r"\uparrow").scale(2).move_to(plane.c2p(-4, -1.4)).set_color(GREEN)
        arrow_text2 = MathTex(r"\uparrow").scale(2).move_to(plane.c2p(-4, -1.4)).set_color(GREEN)
        arrow_text3 = MathTex(r"\uparrow").scale(2).move_to(plane.c2p(-3, -1.4))
        text_min = always_redraw(lambda: Tex("min").next_to(arrow_text2, DOWN, buff=0.2).set_color(GREEN))

        self.play(Create(items), run_time=1.5)  # display the integers
        self.play(Write(text_group2))
        self.play(Write(arrow_text1), Write(arrow_text2), Write(arrow_text3), Write(text_min))

        def selection_sort(items):
            nonlocal comparison_count
            n = len(items)

            for i in range(n):
                min_index = i

                for j in range(i+1, n):
                    self.play(
                        arrow_text1.animate.move_to(plane.c2p(-4+i, -1.4)),
                        arrow_text2.animate.move_to(plane.c2p(-4+min_index, -1.4)),
                        arrow_text3.animate.move_to(plane.c2p(-4+j, -1.4))
                    )
                    comparison_count += 1

                    if items[j][1].get_value() < items[min_index][1].get_value():
                        min_index = j
                        self.play(arrow_text2.animate.move_to(plane.c2p(-4+min_index, -1.4)))
                
                if i != min_index:
                    # animate the swapping of two numbers
                    self.play(
                        items[i].animate.move_to(items[min_index].get_center()),
                        items[min_index].animate.move_to(items[i].get_center())
                    )
                    # swap them in items
                    items[i], items[min_index] = items[min_index], items[i]

        selection_sort(items)

        self.wait(frozen_frame=False)
