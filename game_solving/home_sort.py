import time

is_found = False
solution = []
count_items = {}


def merge_continuous_items(arr):
    if not arr:
        return []

    result = []
    current_item = arr[0]
    count = 1

    for i in range(1, len(arr)):
        if arr[i] == current_item:
            count += 1
        else:
            result.append([current_item, count])
            current_item = arr[i]
            count = 1

    # Add the last item and its count
    result.append([current_item, count])

    return result


class Cell:
    def __init__(self, cell_len, items):
        self.cell_len = cell_len
        self.raw_len = len(items)
        self.items = merge_continuous_items(items)

    def last(self):
        return self.items[-1]

    def remove(self):
        temp = self.items.pop(-1)
        self.build_raw_len()
        return temp

    def add(self, item):
        if len(self.items) == 0:
            self.items.append(item)
        else:
            if self.items[-1][0] == item[0]:
                self.items[-1][-1] += item[-1]
        self.build_raw_len()

    def build_raw_len(self):
        self.raw_len = sum(i[-1] for i in self.items)

    def can_add(self, item):
        if len(self.items) != 0 and self.items[-1][0] != item[0]:
            return False
        if self.raw_len + item[-1] <= self.cell_len:
            return True
        return False

    def print_raw(self):
        print(' '.join([(i[0] + ' ') * i[-1] for i in self.items]))

    def print(self):
        print(' '.join(str(i) for i in self.items))

    def check_oke(self):
        global count_items
        return len(self.items) == 1 and self.last()[-1] == self.cell_len and count_items[
            self.last()[0]] == self.cell_len

    def hard_add(self, item):
        self.items.append(item)
        self.build_raw_len()

    def hard_remove(self, item):
        self.last()[-1] -= item[-1]
        if self.last()[-1] == 0:
            self.items.pop()
        self.build_raw_len()

    def gen_hash(self):
        return hash((self.cell_len, self.raw_len, ' '.join(str(i) for i in self.items)))


def can_move(cell_1, cell_2):
    if len(cell_1.items) == 0:
        return False
    if cell_2.can_add(cell_1.last()):
        return True
    return False


def move(cell_1, cell_2):
    temp = cell_1.remove()
    cell_2.add(temp)


def print_cells(cells):
    for i, item in enumerate(cells):
        print(i + 1, end=': ')
        item.print()


def undo(cell_1, cell_2, item):
    cell_2.hard_remove(item)
    cell_1.hard_add(item)


def get_hash(cells):
    return hash(tuple(i.gen_hash() for i in cells))


def recursion(steps, hash_dict, cells, n):
    global is_found, solution
    if is_found:
        return
    count_done = len([i for i in cells if i.check_oke()])
    count_not_done = len(count_items) - count_done - 1
    if n+count_not_done >= len(solution):
        return
    hash_cell = get_hash(cells)
    if hash_cell in hash_dict and hash_dict[hash_cell] <= len(steps):
        return
    hash_dict[hash_cell] = len(steps)

    count = 0
    for i in cells:
        if i.check_oke() or len(i.items) == 0:
            count += 1
    if count == len(cells):
        # Stop when found one solution
        # is_found = True
        if len(steps) < len(solution):
            solution = steps[:]
        return

    for i in range(len(cells)):
        for j in range(len(cells)):
            if i != j and not cells[i].check_oke() and not cells[j].check_oke() and can_move(cells[i], cells[j]):
                item = cells[i].last()[:]
                move(cells[i], cells[j])
                steps.append((i + 1, j + 1))
                recursion(steps, hash_dict, cells, n + 1)
                if not is_found:
                    undo(cells[i], cells[j], item)
                    steps.pop()


def main():
    import sys
    sys.stdin = open('lv16.csv', 'r')
    sys.stdout = open('sol_lv16.txt', 'w')
    # test = int(input())
    for _ in range(1):
        global is_found, solution, count_items
        is_found = False
        count_items.clear()
        solution = [i for i in range(300)]
        m = int(input())
        cells = []
        for i in range(m):
            raw = input().split(',')
            for i in raw:
                if i not in count_items:
                    count_items[i] = 0
                count_items[i] += 1
            cells.append(Cell(len(raw), [i for i in raw if i != '_']))
        print_cells(cells)
        hash_dict = {}
        steps = []
        start_time = time.time()
        recursion(steps, hash_dict, cells, 1)
        end_time = time.time()
        print('Solve:', len(solution), 'steps', '-', len(hash_dict), 'states')
        for i, item in enumerate(solution):
            print(i + 1, ':', item)
        # Calculate the elapsed time
        elapsed_time = end_time - start_time
        print(f"Time: {elapsed_time:.4f}")


if __name__ == '__main__':
    main()
