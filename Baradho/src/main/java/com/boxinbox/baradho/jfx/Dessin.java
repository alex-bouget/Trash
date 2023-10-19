package com.boxinbox.baradho.jfx;

import javafx.scene.canvas.Canvas;
import javafx.scene.canvas.GraphicsContext;

public class Dessin extends Canvas {

    GraphicsContext gc;

    public Dessin() {
        super();

        setWidth(com.boxinbox.baradho.Baradho.getLargeur());
        setHeight(com.boxinbox.baradho.Baradho.getHauteur());
        gc = this.getGraphicsContext2D();
    }

    public GraphicsContext getGc() {
        return gc;
    }

    public boolean dessiner() {
        gc.setFill(javafx.scene.paint.Color.BLACK);
        gc.fillRect(0, 0, com.boxinbox.baradho.Baradho.getLargeur(), com.boxinbox.baradho.Baradho.getHauteur());
        return true;
    }
    
}
