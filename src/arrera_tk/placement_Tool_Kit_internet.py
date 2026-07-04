class placement_Tool_Kit_internet:
    def placeCenter(self):
        self.place(relx=0.5, rely=0.5, anchor='center')

    def placeLeftCenter(self):
        self.place(relx=0, rely=0.5, anchor='w')

    def placeRightCenter(self):
        self.place(relx=1, rely=0.5, anchor='e')

    def placeTopCenter(self):
        self.place(relx=0.5, rely=0, anchor='n')

    def placeBottomCenter(self):
        self.place(relx=0.5, rely=1, anchor='s')

    def placeCenterOnWidth(self, y: int = 0):
        if (y == 0):
            return
        else:
            self.place(relx=0.5, y=y, anchor='n')

    def placeWidgetCenteredAtBottom(self, x_offset=1):
        self.place(relx=0.5, rely=1, x=-x_offset, anchor="s")

    def placeBottomRight(self):
        self.place(relx=1, rely=1, anchor='se')

    def placeBottomLeft(self):
        self.place(relx=0, rely=1, anchor='sw')

    def placeTopRight(self):
        self.place(relx=1, rely=0, anchor='ne')

    def placeTopLeft(self):
        self.place(relx=0, rely=0, anchor='nw')

    def placeCenterRight(self):
        self.place(relx=1, rely=0.5, anchor='e')

    def placeCenterLeft(self):
        self.place(relx=0, rely=0.5, anchor='w')

    def placeLeftBottomNoStick(self):
        self.place(relx=0, rely=1, anchor='sw', x=10, y=-10)

    def placeRightBottomNoStick(self):
        self.place(relx=1, rely=1, anchor='se', x=-10, y=-10)

    def placeBottomCenterNoStick(self):
        self.place(relx=0.5, rely=1, anchor='s', x=0, y=-10)

    # Pack

    def pack(self, xExpand: bool = False, yExpand: bool = False, **kwargs):
        if xExpand and yExpand:
            kwargs.update({'expand': True, 'fill': 'both'})
        elif xExpand:
            kwargs.update({'expand': True, 'fill': 'x'})
        elif yExpand:
            kwargs.update({'expand': True, 'fill': 'y'})

        super().pack(**kwargs)

    def packLeft(self, xExpand: bool = False, yExpand: bool = False, **kwargs):
        self.pack(xExpand=xExpand, yExpand=yExpand, side="left", **kwargs)

    def packRight(self, xExpand: bool = False, yExpand: bool = False, **kwargs):
        self.pack(xExpand=xExpand, yExpand=yExpand, side="right", **kwargs)

    def packTop(self, xExpand: bool = False, yExpand: bool = False, **kwargs):
        self.pack(xExpand=xExpand, yExpand=yExpand, side="top", **kwargs)

    def packBottom(self, xExpand: bool = False, yExpand: bool = False, **kwargs):
        self.pack(xExpand=xExpand, yExpand=yExpand, side="bottom", **kwargs)
