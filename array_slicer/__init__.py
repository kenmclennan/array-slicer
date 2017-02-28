class ArraySlicer:
    def __init__(self, array):
        self.array = array

    def slice_into(self, slices):
        if (slices < 0):
            raise ValueError("was asked for %d slices, expected a minimum of 0" % slices)

        if (slices == 0):
            return []

        slice_base_size, remaining = divmod(len(self.array), slices)

        cursor = 0
        output = []

        for index in range(slices):
            slice_size = slice_base_size
            if (index < remaining):
                slice_size += 1

            slice_start = cursor
            slice_end   = slice_start + slice_size
            cursor      = slice_end

            output.append(self.array[slice_start:slice_end])

        return output