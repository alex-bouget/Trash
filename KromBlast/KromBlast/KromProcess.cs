using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Diagnostics;
using Microsoft.Web.WebView2;
using System.Threading;

namespace KromBlast
{
    internal class KromProcess
    {
        String id;
        Process myCmd;
        Microsoft.Web.WebView2.WinForms.WebView2 webView;

        public KromProcess(String id, Microsoft.Web.WebView2.WinForms.WebView2 webView)
        {
            this.id = id;
            this.webView = webView;
            myCmd = createConsole();
            Thread thread = new Thread(looper);
        }

        public async void looper()
        {
            myCmd.StandardInput.WriteLine("echo test");
            while (true)
            {
                Console.WriteLine(myCmd.StandardOutput.ReadLine());
            }
        }


        private Process createConsole()
        {
            ProcessStartInfo startInfo = new ProcessStartInfo();
            startInfo.UseShellExecute = false; //required to redirect standart input/output

            // redirects on your choice
            startInfo.RedirectStandardOutput = true;
            startInfo.RedirectStandardOutput = true;
            startInfo.RedirectStandardError = true;

            startInfo.FileName = "cmd";
            // startInfo.Arguments = "";

            Process process = new Process();
            process.StartInfo = startInfo;
            process.Start();
            return process;

            //process.StandardInput.WriteLine("");
        }
    }
}
