using Microsoft.Web.WebView2.Core;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace KromBlast
{
    public partial class KromForm : Form
    {
        Dictionary<String, KromProcess> myProcess = new Dictionary<string, KromProcess>();

        public KromForm()
        {
            InitializeComponent();
            MaximumSize = new Size(
                Screen.PrimaryScreen.WorkingArea.Width,
                Screen.PrimaryScreen.WorkingArea.Height
                );
        }

        public void AddProcess()
        {

        }

        private void KromForm_SizeChanged(object sender, EventArgs e)
        {
            Viewer.Width = Width;
            Viewer.Height = Height;
        }
    }
}
