package com.boxinbox.baradho.menu;

import com.boxinbox.baradho.Core.ICore;
import com.boxinbox.baradho.jfx.IElement;

public interface IMenu extends IElement {
    public IButton getSelectedButton();

    public boolean isButtonSelected();

    public void menuLoop(ICore i);
}
