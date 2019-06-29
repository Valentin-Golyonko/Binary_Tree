import tkinter as tk

import matplotlib.pyplot as plt
import numpy as np

from log.Log_Color import *


class Student:
    def __init__(self, _name, _score):
        """
        Define student parameters: name, score, next student position to the left/right.

        :param _name: student name
        :param _score: student score
        """
        self.name = _name
        self.__score__ = _score
        self.right = None
        self.left = None

    @property
    def score_p(self):
        return self.__score__

    @score_p.setter
    def score_p(self, value):
        raise Exception("You can NOT change student score!")

    @score_p.deleter
    def score_p(self):
        raise Exception("You can NOT change student score!")


class Tree:
    def __init__(self, _root):
        """
        Operations with tree:
        set root student, add student, find, find_all, dell, dell_all, plot tree.
        Find+/dell+ methods accepts score value and tree root.

        :param _root: binary tree root
        """
        self.root = _root

        self.arr_find_all = []
        self.arr_dell = []
        self.__add_count__ = 0  # tree depth (for plot correction)
        self.__coords__ = []  # nodes position
        self.__x__ = 0
        self.__y__ = 0
        self.__p__ = 0  # x coordinate of the parent node (root)
        self.__names__ = []  # nodes names
        self.__root_saved__ = 0  # remember tee root
        self.__root_flag__ = ""  # for each student set branch direction (left/right) from main root

    def add(self, new_student):
        """
        :param new_student: Student('name', _score)
        """
        count = 0
        cur = self.root
        while True:
            count += 1
            if new_student.score_p > cur.score_p:  # right
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = new_student
                    break
            else:  # left
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = new_student
                    break
        self.__add_count__ = max(self.__add_count__, count)

    def child(self, _root):
        """
        Search which child (_root.left or _root.right) will be better to replace current parent (_root).

        :param _root: current root
        :return: "left" - left score better, "right" - right score better or 1 - no children
        """
        rls, rrs = 0, 0
        if _root.left:  # if _root has children
            rls = _root.left.score_p
        if _root.right:
            rrs = _root.right.score_p

        if rls < rrs and rls != 0:  # check children score, select max value
            return _root.left, "l"  # Tuple('best child' to replace current root, child position left or right)
        elif rrs < rls and rrs != 0:
            return _root.right, "r"
        elif rrs > rls:
            return _root.right, "r"
        elif rls > rrs:
            return _root.left, "l"
        else:
            return None, 1

    def dell(self, _score, _root, _all=False):
        """
        Delete student/s by score with replacement.
        Search which child will be better to replace current parent and do it.
        Check score and go only to the left or right on the branch.
        If _all = True - go deep to the last with this score, return, delete all previous with this score.

        :param _score: student score
        :param _root: root student
        :param _all: delete all with this score or not
        :return: No! too complicated...
        """
        if not _all and _root.score_p == _score:  # else: go deeper
            self.arr_dell.append([_root.name, _root.score_p])  # or returns the first student found

            return self.child(_root)

        if _root.left and _score <= _root.score_p:

            _, ret_l = self.dell(_score, _root.left, _all)  # recursion

            if ret_l == "l":
                ll_rrl = _root.left.left  # get child object
                better_child_ll, _ = self.child(ll_rrl)  # set child root.lift.left

                ll_rrr = None
                if _root.left.right:
                    ll_rrr = _root.left.right

                _root.left = ll_rrl  # replace deleted student position with his child
                _root.left.right = ll_rrr  # set child root.right.right
                _root.left.left = better_child_ll

                if not _all:
                    return None, 0

            elif ret_l == "r":
                lr_rrr = _root.left.right
                better_child_lr, _ = self.child(lr_rrr)

                lr_rrl = None
                if _root.left.left:
                    lr_rrl = _root.left.left

                _root.left = lr_rrr
                _root.left.left = lr_rrl
                _root.left.right = better_child_lr

                if not _all:
                    return None, 0

            elif ret_l == 1:
                _root.left = None
                if not _all:
                    return None, 0

        if _root.right and _score >= _root.score_p:

            _, ret_r = self.dell(_score, _root.right, _all)  # recursion

            if ret_r == "l":
                rl_rrl = _root.right.left
                better_child_rl, _ = self.child(rl_rrl)

                rl_rrr = None
                if _root.right.right:
                    rl_rrr = _root.right.right

                _root.right = rl_rrl
                _root.right.right = rl_rrr
                _root.right.left = better_child_rl

                if not _all:
                    return None, 0

            elif ret_r == "r":
                rr_rrr = _root.right.right
                better_child_rr, _ = self.child(rr_rrr)

                rr_rrl = None
                if _root.right.left:
                    rr_rrl = _root.right.left

                _root.right = rr_rrr
                _root.right.left = rr_rrl
                _root.right.right = better_child_rr

                if not _all:
                    return None, 0

            elif ret_r == 1:
                _root.right = None
                if not _all:
                    return None, 0

        if _root.score_p == _score and _all:  # we found last student with required score
            self.arr_dell.append([_root.name, _root.score_p])

            return self.child(_root)

        return None, 0

    def find(self, _score, _root):
        """
        Find student by score.
        Check score and go only to the left or right on the branch.

        :param _score: Student score
        :param _root: tree root
        :return: Tuple(student name, student score)
        """
        if _root.score_p == _score:
            return _root.name, _root.score_p

        if _root.left and _score < _root.score_p:
            return self.find(_score, _root.left)  # recursion

        if _root.right and _score > _root.score_p:
            return self.find(_score, _root.right)  # recursion

    def find_all(self, _score, _root):
        """
        Find all students with this score.
        Check score and go only to the left or right on the branch.

        :param _score: students score
        :param _root: tree root
        :return: No! cause 2 recursion
        """
        if _root.score_p == _score:
            self.arr_find_all.append([_root.name, _root.score_p])

        if _root.left and _score <= _root.score_p:
            self.find_all(_score, _root.left)  # recursion

        if _root.right and _score >= _root.score_p:
            self.find_all(_score, _root.right)  # recursion

    def print_tree(self, _root):
        """
        Find Tree branches and leaves, and print whole tree to console.
        Fill in the list with the parameters of students
        ['name', score, coord x, coord y, parent coord x, 'branch flag'].
        Add objects 1 by 1 to the dictionary.

        :param _root: root student
        :return: No! cause 2 recursion
        """
        self.__names__.append([_root.name, _root.score_p, self.__x__, self.__y__, self.__p__, self.__root_flag__])
        log_info("\t%s %s" % (_root.name, self.__names__[-1]))

        if _root.right and _root.right is not None:
            if _root == self.__root_saved__:
                self.__root_flag__ = "r"
            self.__p__ = self.__x__  # magic ™
            self.__x__ += 1
            self.__y__ -= 1
            self.print_tree(_root.right)  # recursion
            self.__x__ -= 1  # magic ™
            self.__y__ += 1
            self.__p__ = self.__x__

        if _root.left and _root.left is not None:
            if _root == self.__root_saved__:
                self.__root_flag__ = "l"
            self.__p__ = self.__x__  # magic ™
            self.__x__ -= 1
            self.__y__ -= 1
            self.print_tree(_root.left)  # recursion
            self.__x__ += 1  # magic ™
            self.__y__ += 1
            self.__p__ = self.__x__

    def print_empty_leaves(self, _root):
        """
        Print 'leaves' without 'children', empty leaves

        :param _root: root student
        :return: No! cause 2 recursion
        """
        if not _root.left and not _root.right:
            log_info("\tprint_empty_leaves: %s, %s" % (_root.name, _root.score_p))
        if _root.right:
            self.print_empty_leaves(_root.right)  # recursion
        if _root.left:
            self.print_empty_leaves(_root.left)  # recursion

    def visual(self):
        """
        Plot tree with matplotlib.

        BUG 🚩: points on the graph intersect
        """
        log_verbose("visual()")

        an = np.linspace(0, 2 * np.pi, 100)
        fig, axs = plt.subplots()

        fig.set_size_inches(10, 5)
        axs.clear()
        axs.set_axis_off()

        def text(px, py, _text):
            axs.text(px, py, _text, backgroundcolor="white", ha='center', va='top', color='black')  # weight='bold'

        correction = 0

        for i in self.__names__:
            if i[2] == 0 and i[3] == 0:
                axs.plot(0 + .4 * np.cos(an), 0 + .4 * np.sin(an))  # circle
                text(0, 0, "%s, %s" % (i[0], i[1]))  # student name and score
                plt.pause(.15)
                continue

            if i[5] == "r":  # right branch
                correction = self.__add_count__ - 1
            elif i[5] == "l":  # left branch
                correction = - self.__add_count__ + 1

            x2 = i[2] + correction
            y2 = i[3]

            if y2 == -1:  # first branches
                x1 = i[4]
            else:
                x1 = i[4] + correction

            y1 = y2 + 1

            axs.plot(x2 + .4 * np.cos(an), y2 + .4 * np.sin(an))  # circle
            text(x2, y2, "%s, %s" % (i[0], i[1]))  # student name and score
            plt.pause(.15)  # sleep
            axs.plot([x1, x2], [y1, y2])  # line
            plt.pause(.15)  # sleep

        self.__make_var_zero__()

        plt.show()

    def __make_var_zero__(self):
        """
        Set to zero necessary variables
        """
        log_verbose("__make_var_zero__()")
        self.__names__.clear()
        self.__x__, self.__y__, self.__p__ = 0, 0, 0
        self.arr_dell.clear()
        self.arr_find_all.clear()
        self.__root_saved__ = 0
        self.__root_flag__ = ""


class Gui:
    def __init__(self):
        """
        Run predefined config.
        But you can work and change it in the GUI window.
        """
        m1, m2 = main()
        self.__root_student_gui__ = m1
        self.__root_tree_gui__ = m2
        self.__root_tree_gui__.__make_var_zero__()

    def gui(self):
        """
        2 edit lines:
        1st - enter root student (name, score);
        2d - enter student name or score to add (name, score) or dell or find (by name or score);
        6 buttons - add root (name, score), dell/dell_all (by score), search/search_all (by score).
        """
        log_verbose("gui()")

        root_gui = tk.Tk()
        root_gui.title("Binary tree")
        root_gui.minsize(width=300, height=350)

        lb_path = tk.Label(text="Please enter root student - name score:", width=50)
        lb_path.grid(row=0, columnspan=3, padx=4, pady=4)

        en_root = tk.Entry()
        en_root.insert(0, "%s %s" % (self.__root_student_gui__.name, self.__root_student_gui__.score_p))
        en_root.grid(row=1, columnspan=3, padx=4, pady=4)

        btn_add_root = tk.Button(text="Add root", bg="orange")
        btn_add_root.grid(row=2, columnspan=3, padx=4, pady=4)

        lb_hello = tk.Label(text="Please Enter student score you want to dell/find"
                                 "\nor enter student name score to add:", width=50)
        lb_hello.grid(row=3, columnspan=3, padx=4, pady=4)

        en_search = tk.Entry()
        en_search.grid(row=4, columnspan=3, padx=4, pady=4)

        btn_add = tk.Button(text="Add", bg="orange")
        btn_add.grid(row=5, column=0, padx=4, pady=4)

        btn_dell = tk.Button(text="Dell", bg="orange")
        btn_dell.grid(row=5, column=1, padx=4, pady=4)

        btn_dell_all = tk.Button(text="Dell all", bg="orange")
        btn_dell_all.grid(row=6, column=1, padx=4, pady=4)

        btn_search = tk.Button(text="Search", bg="orange")
        btn_search.grid(row=5, column=2, padx=4, pady=4)

        btn_search_all = tk.Button(text="Search all", bg="orange")
        btn_search_all.grid(row=6, column=2, padx=4, pady=4)

        lb_output = tk.Label(wraplength=400, justify="center")
        lb_output.grid(row=7, columnspan=3, padx=4, pady=4)

        def add_root(event):
            """init Root and Tree"""
            get_text = en_root.get().split()
            if len(get_text) > 0:
                log_info("\tgui_add_root: %s" % get_text)
                try:
                    self.__root_student_gui__ = Student(get_text[0], float(get_text[1]))
                    self.__root_tree_gui__ = Tree(self.__root_student_gui__)

                    lb_output["text"] = "Root student %s added" % get_text
                    self.__after_action__()

                except Exception as ex:
                    lb_output["text"] = "Ex: %s \nTry to enter: Name and score like 'Man 7'" % ex
                    log_error(ex)
            else:
                lb_output["text"] = "enter something"

        def fun_add(event):
            """tree.add(Student('Egor', 6.5))"""
            get_text = en_search.get().split()
            if len(get_text) > 0:
                log_info("\tgui_fun_add: %s" % get_text)
                try:
                    self.__root_tree_gui__.add(Student(get_text[0], float(get_text[1])))

                    lb_output["text"] = "Student %s %s added" % (get_text[0], get_text[1])
                    log_info("Student %s %s added" % (get_text[0], get_text[1]))
                    self.__after_action__()

                except Exception as ex:
                    lb_output["text"] = "Ex: %s \nTry to enter: Name and score like 'Mike 8.7'" % ex
                    log_error(ex)
            else:
                lb_output["text"] = "enter something"

        def fun_dell(event):
            """tree.dell(4, root_student)"""
            get_text = en_search.get()
            if len(get_text) > 0:
                log_info("\tgui_fun_dell: %s" % get_text)
                try:
                    self.__root_tree_gui__.dell(float(get_text), self.__root_student_gui__)

                    arr_d = self.__root_tree_gui__.arr_dell
                    if len(arr_d) > 0:

                        lb_output["text"] = "Student %s deleted" % arr_d
                        log_warning("\tdell: %s" % arr_d)
                        self.__after_action__()

                    else:
                        lb_output["text"] = "Nothing found, \n Try again ;)"
                except Exception as ex:
                    lb_output["text"] = "Ex: %s" % ex
                    log_error(ex)
            else:
                lb_output["text"] = "enter something"

        def fun_dell_all(event):
            """tree.dell(3, root_student, True)"""
            get_text = en_search.get()
            if len(get_text) > 0:
                log_info("\tgui_fun_dell: %s" % get_text)
                try:
                    self.__root_tree_gui__.dell(float(get_text), self.__root_student_gui__, True)

                    arr_d = self.__root_tree_gui__.arr_dell
                    if len(arr_d) > 0:

                        lb_output["text"] = "Students %s with score %s deleted" % (arr_d, get_text)
                        log_info("\tdell_all: %s" % arr_d)
                        self.__after_action__()

                    else:
                        lb_output["text"] = "Nothing found, \n Try again ;)"
                except Exception as ex:
                    lb_output["text"] = "Ex: %s" % ex
                    log_error(ex)
            else:
                lb_output["text"] = "enter something"

        def fun_search(event):
            """tree.find(7, root_student)"""
            get_text = en_search.get()
            if len(get_text) > 0:
                log_info("\tgui_fun_search: %s" % get_text)
                try:
                    f_n, f_s = self.__root_tree_gui__.find(float(get_text), self.__root_student_gui__)

                    if len(f_n) > 0:
                        lb_output["text"] = "Student '%s' found, score = %s:" % (f_n, f_s)
                        log_info("\t%s has %s" % (f_n, f_s))

                        self.__after_action__()
                    else:
                        lb_output["text"] = "Nothing found, \n Try again ;)"
                except Exception as ex:
                    lb_output["text"] = "Ex: %s" % ex
                    log_error(ex)
            else:
                lb_output["text"] = "enter something"

        def fun_search_all(event):
            """tree.find_all(6.4, root_student)"""
            get_text = en_search.get()
            if len(get_text) > 0:
                log_info("\tgui_fun_search: %s" % get_text)
                try:
                    self.__root_tree_gui__.find_all(float(get_text), self.__root_student_gui__)

                    arr_f = self.__root_tree_gui__.arr_find_all
                    if len(arr_f) > 0:
                        lb_output["text"] = "Students %s with score %s found:" % (arr_f, get_text)
                        log_info("\t%s has: %s" % (get_text, self.__root_tree_gui__.arr_find_all))

                        self.__after_action__()
                    else:
                        lb_output["text"] = "Nothing found, \n Try again ;)"
                except Exception as ex:
                    lb_output["text"] = "Ex: %s" % ex
                    log_error(ex)
            else:
                lb_output["text"] = "enter something"

        btn_add_root.bind("<Button-1>", add_root)
        btn_add.bind("<Button-1>", fun_add)
        btn_dell.bind("<Button-1>", fun_dell)
        btn_dell_all.bind("<Button-1>", fun_dell_all)
        btn_search.bind("<Button-1>", fun_search)
        btn_search_all.bind("<Button-1>", fun_search_all)

        self.__after_action__()

        root_gui.mainloop()

    def __after_action__(self):
        """
        Find and plot Tree, clean variables
        """
        log_verbose("__after_action__()")
        self.__root_tree_gui__.__root_saved__ = self.__root_student_gui__
        self.__root_tree_gui__.print_tree(self.__root_student_gui__)
        self.__root_tree_gui__.visual()


def main():
    """
    Create root_student, tree. Add 15 students.
    Do find(), find_all(), dell(), dell_all(), plot tree.

    :return: root student, tree
    """
    log_verbose("main()")

    root_student = Student('Boris', 6)
    tree = Tree(root_student)

    # add
    tree.add(Student('Egor', 6.5))
    tree.add(Student('Pavel', 5))
    tree.add(Student('Sergey', 6.6))
    tree.add(Student('Vlad', 6.4))
    tree.add(Student('Gena', 6.4))
    tree.add(Student('Stas', 6.7))
    tree.add(Student('Vova', 6.6))
    tree.add(Student('Lesha', 6.5))
    tree.add(Student('Denis', 5.5))
    tree.add(Student('Sasha', 5.7))
    tree.add(Student('Nikita', 5.3))
    tree.add(Student('Masha', 4.5))
    tree.add(Student('Ola', 4.3))
    tree.add(Student('Sveta', 4.8))

    log_info("\tadd_count: %s" % tree.__add_count__)

    # find
    f_n, f_s = tree.find(6.6, root_student)
    log_info("\t%s has %s" % (f_n, f_s))

    f_n, f_s = tree.find(6.4, root_student)
    log_info("\t%s has %s" % (f_n, f_s))

    # find all
    tree.find_all(6.4, root_student)
    log_info("\t6.4 has: %s" % tree.arr_find_all)
    tree.arr_find_all.clear()

    tree.find_all(6.5, root_student)
    log_info("\t6.5 has: %s" % tree.arr_find_all)
    tree.arr_find_all.clear()

    # dell
    tree.dell(6.6, root_student)
    log_warning("\tdell: %s" % tree.arr_dell)
    tree.arr_dell.clear()

    tree.dell(5.5, root_student)
    log_warning("\tdell: %s" % tree.arr_dell)
    tree.arr_dell.clear()

    tree.dell(4.8, root_student)
    log_warning("\tdell: %s" % tree.arr_dell)
    tree.arr_dell.clear()

    # dell all
    tree.dell(6.4, root_student, True)
    log_warning("\tdell_all: %s" % tree.arr_dell)
    tree.arr_find_all.clear()

    tree.__root_saved__ = root_student
    tree.print_tree(root_student)

    tree.print_empty_leaves(root_student)

    return root_student, tree


if __name__ == "__main__":
    show = Gui()
    show.gui()
