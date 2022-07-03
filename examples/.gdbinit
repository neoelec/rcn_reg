source ~/.config/rcn_reg/gdb_rcn_reg_aarch64.py

set prompt \033[31m(\033[90mgdb\033[31m) \033[0m

set disassemble-next-line off

define hook-stop
    rcn_reg
    printf "\n"
    disassemble $pc,+1
    printf "\n"
end
