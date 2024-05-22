#!/usr/bin/env -S python3 -B

from time import time
from common.tk_drawer import TkDrawer, x, y
import sys
try:
    exec(f'from optimize_{sys.argv[1]}.polyedr import Polyedr')
except (IndexError, ModuleNotFoundError):
    print("\nНеобходимо указание варианта оптимизации от 1 до 7, например,\n"
          "    ./run_optimize 1\n"
          "или\n"
          "    python run_optimize 1\n")
    exit(1)


def draw_line(self, p, q, color="black", width=1):
    self.canvas.create_line(x(p), y(p), x(q), y(q), fill=color, width=width)


setattr(TkDrawer, 'draw_line', draw_line)

tk = TkDrawer()

try:
    for name in ["task64", "ccc", "cube", "box", "king", "cow"]:
        print("=======================================================")
        print(f"Начало работы с полиэдром '{name}'")
        start_init_time = time()
        print("Инициализация -------------------------> ", end="", flush=True)
        poly = Polyedr(f"data/{name}.geom")
        start_optimize_time = time()
        print("%6.2f сек." % (start_optimize_time - start_init_time))
        print("Оптимизация ---------------------------> ", end="", flush=True)
        optimize_statistics = poly.optimize()
        start_shadow_time = time()
        print("%6.2f сек.\n%s" % (start_shadow_time -
                                  start_optimize_time, optimize_statistics))
        print("Удаление невидимых линий --------------> ", end="", flush=True)
        poly.shadow()
        start_draw_time = time()
        print("%6.2f сек." % (start_draw_time - start_shadow_time))
        print("Изображение полиэдра ------------------> ", end="", flush=True)
        poly.draw(tk)
        tk.root.update()
        start_solve64_time = time()
        print("%6.2f сек." % (start_solve64_time - start_draw_time))
        print("Расчет длинны для задания №64 ---------> ", end="", flush=True)
        answer = poly.solve_task64(tk)
        tk.root.update()
        print("%6.2f сек.\n   Ответ на задачу №64: %s"
              % (time() - start_solve64_time, answer))
        input("Hit 'Return' to continue -> ")
except (EOFError, KeyboardInterrupt):
    print("\nStop")
    tk.close()
