from LineUp import LineUp

if __name__ == "__main__":
    inter = LineUp(lum="../lumodule/module.lum", m_dir="../lumodule", e_type="return")
    print(inter.global_variable["l"].execute("../script exemple/script-exemple.lup"))
