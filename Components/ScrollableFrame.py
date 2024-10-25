import tkinter as tk

class ScrollableFrame(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        canvas = tk.Canvas(self)
        scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=canvas.yview)
        self.scrollable_frame = tk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox(tk.ALL)
            )
        )

        self.bind_all("<MouseWheel>",
            lambda event: canvas.configure(
                canvas.yview_scroll(int(-1*(event.delta)), "units")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor=tk.NW)

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)