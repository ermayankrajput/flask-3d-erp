#!/usr/bin/env python3

# $Id$

# Copyright (C) 2008-2014, Roman Lygin. All rights reserved.
# Copyright (C) 2014-2023, CADEX. All rights reserved.

# This file is part of the CAD Exchanger software.

# You may use this file under the terms of the BSD license as follows:

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# * Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.


import sys
from pathlib import Path
import os


import cadexchanger.CadExCore as cadex

sys.path.append(os.path.abspath(os.path.dirname(Path(__file__).resolve()) + r"/../../"))


def main_fun(thePart: cadex.ModelData_Part):
    anAbsolutePathToRuntimeKey = os.path.abspath(os.path.dirname(Path(__file__).resolve()) + r"/runtime_key.lic")
    if not cadex.LicenseManager.CADExLicense_ActivateRuntimeKeyFromAbsolutePath(anAbsolutePathToRuntimeKey):
        print("Failed to activate CAD Exchanger license.")
        return 1
    # aModel = cadex.ModelData_Model()

    # # print("Conversion started...")
    # aReader = cadex.ModelData_ModelReader()
    # # Opening and converting the file
    # if not aReader.Read(cadex.Base_UTF16String('uploads/transported/1687005859172259output1_stp.stl'), aModel):
    #     print("Failed to open and convert the file ")
    #     return 1
    
    # breakpoint()s
    # aCylinder = cadex.ModelAlgo_TopoPrimitives.CreateCylinder(5.0, 10.0)
    aData =  cadex.ModelAlgo_ValidationProperty()

    # Compute Properties
    aSurfaceArea = cadex.ModelAlgo_ValidationProperty.ComputeSurfaceArea(thePart)

    aVolume = cadex.ModelAlgo_ValidationProperty.ComputeVolume(thePart)

    aCentroid = cadex.ModelData_Point()
    cadex.ModelAlgo_ValidationProperty.ComputeCentroid(thePart, aCentroid)

    aBBox = cadex.ModelData_Box()
    cadex.ModelAlgo_BoundingBox.Compute(cadex.ModelData_BRepRepresentation(thePart), aBBox)
        
    # Output properties
    print(f"Surface area: {aSurfaceArea}")
    print(f"Volume:       {aVolume}")
    print(f"Centroid:     ({aCentroid.X()}, {aCentroid.Y()}, {aCentroid.Z()})")
    print(f"Bounding Box: ({aBBox.XRange()}, {aBBox.YRange()}, {aBBox.ZRange()})")
    
    print("Completed")
    return 0

main_fun('aaa.stl')