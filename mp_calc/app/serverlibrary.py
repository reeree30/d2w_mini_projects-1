

def merge(array, p, q, r, byfunc):
    nleft = q - p + 1
    nright = r - q
    left_array = array[p:q+1]
    right_array = array[q+1:r+1]
    left = 0 # use 'p' if you don't slice
    right = 0 # use 'q + 1' if you don't slice
    sorted_pos = p

    while left < nleft and right < nright:
        if byfunc(left_array[left]) < byfunc(right_array[right]) or (byfunc(left_array[left]) == byfunc(right_array[right]) and left_array[left] < right_array[right]):
            #sort in place
            array[sorted_pos] = left_array[left]
            left += 1
        else:
            array[sorted_pos] = right_array[right]
            right += 1
        sorted_pos += 1
    while left < nleft:
        array[sorted_pos] = left_array[left]
        left += 1
        sorted_pos += 1
    while right < nright:
        array[sorted_pos] = right_array[right]
        right += 1
        sorted_pos += 1

def mergesort_recursive(array, p, r, byfunc):

    # recursive case
    if p < r:
        # get the mid point
        q = (p + r) // 2
        # get the new p and r for the left array
        # call merge sort on the left
        mergesort_recursive(array, p, q, byfunc)
        # call the merge sort on the right
        mergesort_recursive(array, q + 1, r, byfunc)
        # call merge function
        merge(array, p, q, r, byfunc)

def mergesort(array, byfunc = None):
    mergesort_recursive(array, 0, len(array) - 1, byfunc)

class Stack:

    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)
        pass

    def pop(self):
        if len(self.__items) >= 1:
            return self.__items.pop()
        pass

    def peek(self):
        if self.__items == []:
            return None
        else:
            return self.__items[-1]
        pass

    def my_show_all(self):
        return (self.__items)

    @property
    def is_empty(self):
        if self.__items == []:
            return True
        else:
            return False
        pass

    @property
    def size(self):
        return len(self.__items)
        pass


class EvaluateExpression:
  # copy the other definitions
  # from the previous parts
    valid_char = '0123456789+-*/() '
    def __init__(self, string=""):
        self.expression = string
    @property
    def expression(self):
        return self.expr
    @expression.setter
    def expression(self, new_expr):
        if new_expr == "":
            self.expr = ""
        else:
            for char in new_expr:
                if char not in self.valid_char:
                    self.expr = ""
                    break
                else:
                    self.expr = new_expr

    def insert_space(self):
        res_expr = ""
        for char in self.expression:
            res_expr += char if char not in "/*+-()" else f" {char} "
        return res_expr

    def process_operator(self, operand_stack, operator_stack):
        right_no = operand_stack.pop()
        left_no = operand_stack.pop()
        operator = operator_stack.pop()
        if operator == "+":
            total = left_no + right_no
        elif operator == "-":
            total = left_no - right_no

        elif operator == "*":
            total = left_no * right_no

        elif operator == "/":
            total = left_no // right_no

        operand_stack.push(total)
    def evaluate(self):
       operand_stack = Stack()
       operator_stack = Stack()
       expression = self.insert_space()
       tokens = expression.split()

       for ch in expression:
           if ch not in "/*+-()":
               operand_stack.push(ch)
           elif ch in "(":
               operator_stack.push(ch)
           elif ch in ")":
               operator_stack.push(ch)


def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]
