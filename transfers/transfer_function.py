# # $Id$

# # Copyright (C) 2008-2014, Roman Lygin. All rights reserved.
# # Copyright (C) 2014-2023, CADEX. All rights reserved.

# # This file is part of the CAD Exchanger software.

# # You may use this file under the terms of the BSD license as follows:

# # Redistribution and use in source and binary forms, with or without
# # modification, are permitted provided that the following conditions are met:
# # * Redistributions of source code must retain the above copyright notice,
# # this list of conditions and the following disclaimer.
# # * Redistributions in binary form must reproduce the above copyright notice,
# # this list of conditions and the following disclaimer in the documentation
# # and/or other materials provided with the distribution.

# # THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# # AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# # IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# # ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# # LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# # CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# # SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# # INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# # CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# # ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# # POSSIBILITY OF SUCH DAMAGE.

# import sys
# from pathlib import Path
# import os
# from pdf2image import convert_from_path
# import cadexchanger.CadExCore as cadex

# sys.path.append(os.path.abspath(os.path.dirname(Path(__file__).resolve()) + r"/../../"))
# import cadex_license as license

# def cadex_Converter(theSource = 'abc.stp', newFileName='abc.stp'):

#     aKey = license.Value()

#     if not cadex.LicenseManager.Activate(aKey):
#         # print("Failed to activate CAD Exchanger license.")
#         return 1

#     aModel = cadex.ModelData_Model()

#     # print("Conversion started...")
#     aReader = cadex.ModelData_ModelReader()
#     # Opening and converting the file
#     if not aReader.Read(cadex.Base_UTF16String(theSource), aModel):
#         # print("Failed to open and convert the file source" + theSource)
#         return 1

#     aWriter = cadex.ModelData_ModelWriter()
#     # Converting and writing the model to file
#     if not aWriter.Write(aModel, cadex.Base_UTF16String('uploads/'+newFileName+'.stl')):
#         #  print("Failed to convert and write the file to specified format STL")
#         return 1
    
#     if not aReader.Read(cadex.Base_UTF16String('uploads/'+newFileName+'.stl'), aModel):
#         #  print("Failed to open and convert the file source" + 'uploads/'+newFileName+'.stl')
#         return 1

#     if not aWriter.Write(aModel, cadex.Base_UTF16String('uploads/'+newFileName+'.png')):
#         # print("Failed to convert and write the file to specified format pd")
#         return 1    

#     # image = convert_from_path('uploads/'+newFileName+'.pdf')
#     # convert_from_path(image, output_folder='uploads')
#     # pages = convert_from_path('uploads/'+newFileName+'.pdf' , 500)
#     # for count, page in enumerate(pages):
#     #     page.save(f'uploads/'+newFileName+'.pdf.png', 'PNG')

#     # print("Completed")
#     # transportedFile = 'uploads/'+newFileName+'.stl' 
#     # imageFile =  'uploads/'+newFileName+'.png'
#     return True
# # breakpoint()

# # if __name__ == "__main__":
# #     if len(sys.argv) != 3:
# #         # # print("    <input_file>  is a name of the STEP file to be read")
# #         # # print("    <output_file> is a name of the JT file to Save() the model")     
# #         sys.exit()

# #     aSource = os.path.abspath(sys.argv[1])
# #     aDest = os.path.abspath(sys.argv[2])

# #     sys.exit(main(aSource, aDest))

# # main_my()
