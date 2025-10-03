from manim import *

class Algorithm(Scene):
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
        total_swap_count = 0

        text1 = Tex("Insertion count: ")
        num1 = always_redraw(lambda: Integer().set_value(total_swap_count).next_to(text1, RIGHT, buff=0.3))
        text_group1 = VGroup(text1, num1).next_to(items, UP, buff=1.4)

        text2 = Tex("Comparison count: ")
        num2 = always_redraw(lambda: Integer().set_value(comparison_count).next_to(text2, RIGHT, buff=0.3))
        text_group2 = VGroup(text2, num2).next_to(text_group1, UP, buff=0.3)

        arrow_text1 = MathTex(r"\uparrow").scale(2).move_to(plane.c2p(-3, -1.4))
        arrow_text2 = MathTex(r"\uparrow").scale(2).move_to(plane.c2p(-3, -1.4))

        self.play(Create(items), run_time=1.5)  # display the integers
        self.play(Write(text_group1))
        self.play(Write(text_group2))
        self.play(Write(arrow_text1), Write(arrow_text2))

        def insertion_pass(data, already_sorted):  # use array instead of VGroup here, because array has insert and pop method
            nonlocal items
            nonlocal comparison_count
            nonlocal total_swap_count  # similar to items, we declare those count using nonlocal

            a = data[already_sorted]
            status = 0

            for i in range(already_sorted):  # compare a with every element before a

                self.play(arrow_text1.animate.shift(LEFT*1), run_time=0.5)
                
                if data[already_sorted-1-i] < a:  # if we find the first element less than a, insert a after that element

                    comparison_count += 1
                    data.insert(already_sorted-i, data.pop(already_sorted))  # carry out insertion in "data"
                    status += 1

                    self.play(items[already_sorted].animate.shift(UP*1.2), run_time=1)  # move the number at "already_sorted" index up 1 unit
                    moved_group = VGroup()  # pack the numbers that will be moved into a VGroup and shift them left 1 unit
                    if i != 0:  # if i=0, then the insertion has no effect
                        for j in range(i):
                            moved_group.add(items[already_sorted-1-j])
                        self.play(moved_group.animate.shift(RIGHT*1), run_time=1)
                    self.play(items[already_sorted].animate.shift(LEFT*len(moved_group), DOWN*1.2))  # move the number at the top to the desired location

                    element_list = list(items)  # carry out insertion on VGroup "items". Since VGroups do not has .pop() we first convert it to a list and then convert back
                    element_list.insert(already_sorted - i, element_list.pop(already_sorted))
                    items = VGroup(*element_list)  # we assigned value to "items", therefore Python thinks it is a local variable, to prevent this wrote "nonlocal items" at the beginning
                    total_swap_count += 1
                    break
                else:
                    comparison_count += 1

            if status == 0:  # edge case: if a is smaller than every element before a
        
                data.insert(0, data.pop(already_sorted))  # insert a in the beginning of the list

                self.play(items[already_sorted].animate.shift(UP*1.2), run_time=1)  # move to left by 1 unit
                moved_group = VGroup()
                for j in range(already_sorted):
                    moved_group.add(items[j])
                self.play(moved_group.animate.shift(RIGHT*1), run_time=1)
                self.play(items[already_sorted].animate.shift(LEFT*len(moved_group), DOWN*1.2))

                element_list = list(items)  # carry out insertion
                element_list.insert(0, element_list.pop(already_sorted))
                items = VGroup(*element_list)
                total_swap_count += 1

            self.play(
                arrow_text1.animate.move_to(plane.c2p(-3+already_sorted, -1.4)),
                arrow_text2.animate.move_to(plane.c2p(-3+already_sorted, -1.4))
                )


        for i in range(1, len(data)):
            insertion_pass(data, i)