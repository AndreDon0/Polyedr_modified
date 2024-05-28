#!/usr/bin/env -S python3 -B

from time import time
from common.tk_drawer import TkDrawer
from shadow.polyedr import Polyedr


tk = TkDrawer()
try:
    for name in ["ccc", "cube", "box", "king", "cow"]:
        print("=============================================================")
        print(f"Начало работы с полиэдром '{name}'")
        start_time = time()
        poly = Polyedr(f"data/{name}.geom")
        poly.draw(tk)
        start_solve64_time = time()
        print(f"Изображение полиэдра '{name}' заняло {start_solve64_time -
                                                      start_time} сек.")
        print("Расчет длинны для задания №64 ---------> ", end="", flush=True)
        answer = poly.solve_task64(tk)
        tk.root.update()
        print("%6.2f сек.\n   Ответ на задачу №64: %s"
              % (time() - start_solve64_time, answer))

        input("Hit 'Return' to continue -> ")
except (EOFError, KeyboardInterrupt):
    print("\nStop")
    tk.close()
