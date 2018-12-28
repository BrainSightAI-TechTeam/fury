import os
from os.path import join as pjoin
import numpy as np
import numpy.testing as npt
import vtk
from fury.io import load_polydata, save_polydata
from fury.utils import vtk, numpy_support, numpy_to_vtk_points
from fury.tmpdirs import InTemporaryDirectory
from fury.testing import assert_greater


def test_save_and_load_polydata():
    l_ext = ["vtk", "fib", "ply", "xml"]
    fname = "temp-io"

    for ext in l_ext:
        with InTemporaryDirectory() as odir:
            data = np.random.randint(0, 255, size=(50, 3))

            pd = vtk.vtkPolyData()
            pd.SetPoints(numpy_to_vtk_points(data))

            fname_path = pjoin(odir, "{0}.{1}".format(fname, ext))
            save_polydata(pd, fname_path)

            npt.assert_equal(os.path.isfile(fname_path), True)
            assert_greater(os.stat(fname_path).st_size, 0)

            out_pd = load_polydata(fname_path)
            out_data = numpy_support.vtk_to_numpy(out_pd.GetPoints().GetData())

            npt.assert_array_equal(data, out_data)

    npt.assert_raises(IOError, save_polydata, vtk.vtkPolyData(), "test.vti")
    npt.assert_raises(IOError, save_polydata, vtk.vtkPolyData(), "test.obj")
    npt.assert_raises(IOError, load_polydata, "test.vti")


if __name__ == "__main__":
    test_save_and_load_polydata()
