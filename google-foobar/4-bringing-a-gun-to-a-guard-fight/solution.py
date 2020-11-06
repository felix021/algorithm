def calc_distance2(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

def common_divisor(a, b):
    return a if b == 0 else common_divisor(b, a % b)

class Vector(object):
    def __init__(self, a, b):
        x = b[0] - a[0]
        y = b[1] - a[1]
        self.distance2 = x * x + y * y

        cd = common_divisor(abs(x), abs(y))
        self.direction = (x, y) if cd == 0 else (x / cd, y / cd)

class Room(object):
    def __init__(self, left_bottom, right_top, your_position, guard_position):
        self.x1, self.y1 = left_bottom
        self.x2, self.y2 = right_top
        self.you = tuple(your_position)
        self.guard = tuple(guard_position)

    def corners(self):
        return [
            (self.x1, self.y1),
            (self.x1, self.y2),
            (self.x2, self.y1),
            (self.x2, self.y2),
        ]

    def mirror_up(self):
        left_bottom = (self.x1, self.y2)
        right_top   = (self.x2, self.y2 * 2 - self.y1)
        your_position  = (self.you[0], self.y2 * 2 - self.you[1])
        guard_position = (self.guard[0], self.y2 * 2 - self.guard[1])
        return Room(left_bottom, right_top, your_position, guard_position)
    
    def mirror_right(self):
        left_bottom = (self.x2, self.y1)
        right_top   = (self.x2 * 2 - self.x1, self.y2)
        your_position  = (self.x2 * 2 - self.you[0], self.you[1])
        guard_position = (self.x2 * 2 - self.guard[0], self.guard[1])
        return Room(left_bottom, right_top, your_position, guard_position)
    
    def mirror_down(self):
        left_bottom = (self.x1, self.y1 * 2 - self.y2)
        right_top   = (self.x2, self.y1)
        your_position  = (self.you[0], self.y1 * 2 - self.you[1])
        guard_position = (self.guard[0], self.y1 * 2 - self.guard[1])
        return Room(left_bottom, right_top, your_position, guard_position)

    def mirror_left(self):
        left_bottom = (self.x1 * 2 - self.x2, self.y1)
        right_top   = (self.x1, self.y2)
        your_position  = (self.x1 * 2 - self.you[0], self.you[1])
        guard_position = (self.x1 * 2 - self.guard[0], self.guard[1])
        return Room(left_bottom, right_top, your_position, guard_position)

    def mirror_rooms(self):
        return [
            self.mirror_up(),
            self.mirror_right(),
            self.mirror_down(),
            self.mirror_left(),
        ]

    def __hash__(self):
        return hash((self.x1, self.y1, self.x2, self.y2))

    def __eq__(self, other):
        return self.x1 == other.x1 and self.y1 == other.y1 and \
            self.x2 == other.x2 and self.y2 == other.y2

    def __repr__(self):
        return str((self.x1, self.y1, self.x2, self.y2))

def solution(dimensions, your_position, guard_position, distance):
    w, h  = dimensions
    you   = tuple(your_position) # list can't serve as key for dict
    guard = tuple(guard_position)
    max_distance2 = distance ** 2

    forbidden = {}
    possible = {}
    def check_and_update(r):
        v = Vector(you, r.guard)
        if v.direction not in possible or v.distance2 < possible[v.direction]:
            possible[v.direction] = v.distance2
        
        too_far = True
        for p in r.corners() + [r.you]:
            v = Vector(you, p)
            if v.distance2 <= max_distance2:
                too_far = False
            if v.direction not in forbidden or v.distance2 < forbidden[v.direction]:
                forbidden[v.direction] = v.distance2

        return too_far

    def vertical(start, direction):
        cur = start
        while True:
            if direction == "up":
                cur = cur.mirror_up()
            else:
                cur = cur.mirror_down()
            too_far = check_and_update(cur)
            if too_far:
                break

    center = Room((0, 0), (w, h), you, guard)
    check_and_update(center)
    vertical(center, "up")
    vertical(center, "down")

    left_cur = center
    right_cur = center
    while True:
        left_cur = left_cur.mirror_left()
        too_far = check_and_update(left_cur)
        vertical(left_cur, "up")
        vertical(left_cur, "down")

        right_cur = right_cur.mirror_right()
        too_far = check_and_update(right_cur)
        vertical(right_cur, "up")
        vertical(right_cur, "down")

        if too_far:
            break

    cnt = 0
    for direction, distance2 in possible.iteritems():
        if direction not in forbidden or distance2 < forbidden[direction]:
            if distance2 <= max_distance2:
                cnt += 1
    
    return cnt

if __name__ == "__main__":
    import sys

    # my case
    print (solution([3,3], [1,2], [2,1], 4) == 5)
    print (solution([3,3], [1,2], [2,1], 5) == 7)

    # example case 1
    print (solution([3,2], [1,1], [2,1], 4) == 7)

    # example case 2
    print (solution([300,275], [150,150], [185,100], 500) == 9)