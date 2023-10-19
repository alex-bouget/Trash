package com.boxinbox.baradho.menu;

import javafx.scene.canvas.GraphicsContext;


public class Button implements IButton {

    private String text;
    private String data;
    private double x;
    private double y;

    public Button(String text, String data, int xpix, int ypix) {
        this.text = text;
        this.data = data;
        this.x = xpix;
        this.y = ypix;
    }

    @Override
    public boolean dessiner(GraphicsContext g) {
        g.fillText(text, x, y);
        return true;
        
    }

    @Override
    public String getData() {
        return data;
    }
    
}
