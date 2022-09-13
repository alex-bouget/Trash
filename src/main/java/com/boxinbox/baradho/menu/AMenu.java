package com.boxinbox.baradho.menu;

import java.util.ArrayList;

import com.boxinbox.baradho.Core.ICore;
import com.boxinbox.baradho.jfx.BestHandler;

import javafx.scene.canvas.GraphicsContext;
import javafx.scene.input.KeyEvent;

public abstract class AMenu extends BestHandler<KeyEvent> implements IMenu {

    protected IButton selectedButton;
    protected ArrayList<IButton> buttons;
    protected int selectedButtonIndex;

    public AMenu(ArrayList<IButton> buttons) {
        super(KeyEvent.KEY_RELEASED);
        this.buttons = buttons;
        selectedButton = null;
        selectedButtonIndex = 0;
    }

    @Override
    public void handle(KeyEvent event) {
        System.out.println(event.getCode().toString());
        switch (event.getCode()) {
            case UP:
                if (selectedButtonIndex > 0) {
                    selectedButtonIndex--;
                } else {
                    selectedButtonIndex = buttons.size() - 1;
                }
                break;
            case DOWN:
                if (selectedButtonIndex < buttons.size() - 1) {
                    selectedButtonIndex++;
                } else {
                    selectedButtonIndex = 0;
                }
                break;
            case ENTER:
                selectedButton = buttons.get(selectedButtonIndex);
                break;
            default:
                System.out.println("key not handled");
                break;
        }
    }

    @Override
    public IButton getSelectedButton() {
        return selectedButton;
    }

    @Override
    public boolean dessiner(GraphicsContext g) {
        boolean result = true;
        for (IButton button : buttons) {
            g.setFill(javafx.scene.paint.Color.WHITE);
            if (button == buttons.get(selectedButtonIndex)) {
                g.setFill(javafx.scene.paint.Color.RED);
            }
            result &= button.dessiner(g);
        }
        return result;
    }
    
    @Override
    public boolean isButtonSelected() {
        return selectedButton != null;
    }

    @Override
    public void menuLoop(ICore i) {
        selectedButton = null;
        while (!isButtonSelected()) {
            i.waitLoop(50);
            try {
                Thread.sleep(50);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
