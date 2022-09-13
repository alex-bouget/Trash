package com.boxinbox.baradhotest;

import java.util.ArrayList;
import java.util.Arrays;

import com.boxinbox.baradho.Baradho;
import com.boxinbox.baradho.Core.ICore;
import com.boxinbox.baradho.menu.AMenu;
import com.boxinbox.baradho.menu.Button;
import com.boxinbox.baradho.menu.IButton;

import javafx.scene.canvas.GraphicsContext;
import javafx.scene.text.TextAlignment;

public class MenuPrincipale extends AMenu {

        public MenuPrincipale() {
                super(new ArrayList<IButton>(Arrays.asList(
                                new Button(
                                                "Jouer",
                                                "jouer",
                                                (int) Baradho.getLargeur() / 2,
                                                ((int) Baradho.getHauteur() / 4) + ((int) Baradho.getHauteur() / 8)),
                                new Button(
                                                "Options",
                                                "options",
                                                (int) Baradho.getLargeur() / 2,
                                                ((int) Baradho.getHauteur() / 4) + 2 * ((int) Baradho.getHauteur() / 8)),
                                new Button(
                                                "Quitter",
                                                "quitter",
                                                (int) Baradho.getLargeur() / 2,
                                                ((int) Baradho.getHauteur() / 4) + 3 * ((int) Baradho.getHauteur() / 8)))));
        }

        @Override
        public boolean dessiner(GraphicsContext g) {
                g.setTextAlign(TextAlignment.CENTER);
                g.setFill(javafx.scene.paint.Color.WHITE);
                g.fillText("Menu principal", ((int) Baradho.getLargeur()) / 2, ((int) Baradho.getHauteur()) / (buttons.size() + 1));
                return super.dessiner(g);
        }

        @Override
        public void menuLoop(ICore i) {
                super.menuLoop(i);
        }

        
}
