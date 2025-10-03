from manim import *

class Algorithm_bubble(Scene):
    def construct(self):

        data = [2, 4, 5, 1, 3, 9, 6, 8, 7]  # raw unsorted data

        plane = NumberPlane(x_range=[-5, 5], y_range=[-4, 4], x_length=10, y_length=8)  # used to set location
        colors = [RED, GREEN, BLUE, YELLOW, PURPLE, ORANGE, PINK, TEAL, MAROON] # different colors for each number

        items = VGroup()  # items consists mobjects correspond to integers in data
        for i in range(len(data)):
            number = Integer(data[i]).set(height=0.7)
            box = SurroundingRectangle(number, color=colors[i], fill_color=colors[i], fill_opacity=0.3, buff=0.2)
            item = VGroup(box, number).move_to(plane.c2p(-4 + i, 0))
            items.add(item)

        comparison_count = 0  
        total_swap_count = 0

        text1 = Tex("Swap count: ")
        num1 = always_redraw(lambda: Integer().set_value(total_swap_count).next_to(text1, RIGHT, buff=0.3))
        text_group1 = VGroup(text1, num1).next_to(items, UP, buff=1)

        text2 = Tex("Comparison count: ")
        num2 = always_redraw(lambda: Integer().set_value(comparison_count).next_to(text2, RIGHT, buff=0.3))
        text_group2 = VGroup(text2, num2).next_to(text_group1, UP, buff=0.3)

        arrow_text1 = MathTex(r"\uparrow").scale(2).move_to(plane.c2p(-4, -1))
        arrow_text2 = MathTex(r"\uparrow").scale(2).move_to(plane.c2p(-3, -1))
        arrow_group = VGroup(arrow_text1, arrow_text2)

        self.play(Create(items), run_time=1.5)  # display the inetgers
        self.play(Write(text_group1))
        self.play(Write(text_group2))
        self.play(Write(arrow_group))

        for end_index in range(len(data), 1, -1):  # bubble sort algorithm
            swap_count = 0  # used to determine whether to terminate the loop
            for comparison_index in range(0, end_index-1):

                comparison_count += 1
                self.wait(0.3, frozen_frame=False)  # since comparison_count is in always redraw, it will not be changed on screen if frozen frame is set to True in self.wait()

                if items[comparison_index][1].get_value() > items[comparison_index + 1][1].get_value():
                    items[comparison_index], items[comparison_index + 1] = items[comparison_index + 1], items[comparison_index]
                    # swap numbers in items
                    self.play(
                        items[comparison_index].animate.move_to(items[comparison_index+1].get_center()),
                        items[comparison_index+1].animate.move_to(items[comparison_index].get_center())
                    )
                    # swap the numbers shown on screen

                    swap_count += 1
                    total_swap_count += 1
                    self.wait(0.3, frozen_frame=False)

                if comparison_index != end_index-2:  # for the last iteration in the loop, we don't have the shift the arrows
                    self.play(arrow_group.animate.shift(RIGHT*1), run_time=0.5)  # otherwise, shift the arrow to the left
                    self.wait(0.3)

            if swap_count == 0:  # if no swap occurs in a loop, we have finished sorting so terminate the loop
                break  # note that, break will prevent the swap_count to be updated

            self.play(arrow_group.animate.move_to(plane.c2p(-3.5, -1)), run_time=1)
            # the center of arrow_group should be moved to (-3.5, -1) so that the arrows are in correct position

        self.wait(frozen_frame=False)  # wait and allow swap_count to update