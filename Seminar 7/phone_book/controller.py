import book_creator as bw
import book_reader as br
import user_interface as ui

def button():
    if ui.mode_question():
        while ui.add_question():
            bw.add_info()
    else: 
        if ui.read_question():
            br.read_name()
        else: br.read_info()