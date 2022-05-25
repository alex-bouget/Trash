namespace KromBlast
{
    partial class KromForm
    {
        /// <summary>
        /// Variable nécessaire au concepteur.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Nettoyage des ressources utilisées.
        /// </summary>
        /// <param name="disposing">true si les ressources managées doivent être supprimées ; sinon, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Code généré par le Concepteur Windows Form

        /// <summary>
        /// Méthode requise pour la prise en charge du concepteur - ne modifiez pas
        /// le contenu de cette méthode avec l'éditeur de code.
        /// </summary>
        private void InitializeComponent()
        {
            this.Viewer = new Microsoft.Web.WebView2.WinForms.WebView2();
            ((System.ComponentModel.ISupportInitialize)(this.Viewer)).BeginInit();
            this.SuspendLayout();
            // 
            // Viewer
            // 
            this.Viewer.AllowExternalDrop = true;
            this.Viewer.CreationProperties = null;
            this.Viewer.DefaultBackgroundColor = System.Drawing.Color.White;
            this.Viewer.Location = new System.Drawing.Point(0, 0);
            this.Viewer.Name = "Viewer";
            this.Viewer.Size = new System.Drawing.Size(485, 460);
            this.Viewer.Source = new System.Uri("https://google.fr", System.UriKind.Absolute);
            this.Viewer.TabIndex = 1;
            this.Viewer.ZoomFactor = 1D;
            // 
            // KromForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(484, 461);
            this.Controls.Add(this.Viewer);
            this.MaximumSize = new System.Drawing.Size(500, 500);
            this.MinimumSize = new System.Drawing.Size(500, 500);
            this.Name = "KromForm";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "KromBlast";
            this.SizeChanged += new System.EventHandler(this.KromForm_SizeChanged);
            ((System.ComponentModel.ISupportInitialize)(this.Viewer)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private Microsoft.Web.WebView2.WinForms.WebView2 Viewer;
    }
}

