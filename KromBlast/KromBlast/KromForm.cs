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
using System.Threading;

namespace KromBlast
{
    public partial class KromForm : Form
    {
        Dictionary<string, KromProcess> myProcess = new Dictionary<string, KromProcess>();
        Dictionary<string, List<String>> allCommand = new Dictionary<string, List<String>>();
        Thread thread;

        public KromForm()
        {
            InitializeComponent();
            Viewer.Source = new Uri(Tools.BeginSource);
            MaximumSize = new Size(
                Screen.PrimaryScreen.WorkingArea.Width,
                Screen.PrimaryScreen.WorkingArea.Height
                );
            Viewer.ContentLoading += Viewer_ContentLoading;
            //thread = new Thread(looper);
        }

        private static string decodeString(string s)
        {
            return s.Split(new string[] { "\"" }, StringSplitOptions.None)[1];
        } 

        private async void looper(object sender, EventArgs e)
        {
            /*while (Tools.KromRun)
            {*/
                string last = decodeString(await Viewer.ExecuteScriptAsync("KromBlast.getLastCmd()"));
                if (!last.Equals("null"))
                {
                    Console.WriteLine(last);
                    string[] data = last.Split(new string[] { "*:!:*" }, StringSplitOptions.None);
                    allCommand[data[0]].Add(data[1]);
                }
            //}
        }

        public async void Viewer_ContentLoading(object sender, CoreWebView2ContentLoadingEventArgs e)
        {
            await Task.Delay(1000);
            bool isKromBlast = (await Viewer.ExecuteScriptAsync("KromBlast.launch()")).Equals("true");
            if (!isKromBlast)
            {
                return;
            }
            string KromId = decodeString(await Viewer.ExecuteScriptAsync("KromBlast.KromId"));
            if (KromId.Equals("null"))
            {
                return;
            }
            if (!myProcess.ContainsKey(KromId))
            {
                allCommand.Add(KromId, new List<string>());
                myProcess.Add(KromId, new KromProcess(KromId, Viewer, allCommand[KromId]));
            }
            System.Windows.Forms.Timer timer1 = new System.Windows.Forms.Timer();
            timer1.Tick += new EventHandler(looper);
            timer1.Interval = 2000; // in miliseconds
            timer1.Start();
            //thread.Start();
            await Viewer.ExecuteScriptAsync("KromBlast.endLaunch()");
        }

        private void KromForm_SizeChanged(object sender, EventArgs e)
        {
            Viewer.Width = Width;
            Viewer.Height = Height;
        }

        private void KromForm_FormClosing(object sender, FormClosingEventArgs e)
        {
            Tools.KromRun = false;
        }
    }
}
