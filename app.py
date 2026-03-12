import qrcode
from tkinter import Tk, Label, Entry, Button, filedialog, messagebox
from urllib.parse import urlparse
from PIL import Image, ImageTk


class QRCodeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor de Link para QR Code")
        self.root.geometry("420x560")
        self.root.resizable(False, False)

        self.qr_image = None
        self.qr_pil_image = None

        Label(root, text="Cole o link abaixo:", font=("Arial", 12)).pack(pady=10)

        self.link_entry = Entry(root, width=45, font=("Arial", 11))
        self.link_entry.pack(pady=5)

        Button(root, text="Gerar QR Code", command=self.generate_qr, width=20).pack(pady=10)
        Button(root, text="Salvar QR Code", command=self.save_qr, width=20).pack(pady=5)
        Button(root, text="Limpar", command=self.clear_all, width=20).pack(pady=5)

        self.image_label = Label(root)
        self.image_label.pack(pady=20)

        self.result_label = Label(root, text="", wraplength=360, justify="center", font=("Arial", 10))
        self.result_label.pack(pady=10)

    def normalize_url(self, url: str) -> str:
        url = url.strip()
        if not url:
            return ""
        if not url.startswith(("http://", "https://")):
            url = "https://" + url
        return url

    def is_valid_url(self, url: str) -> bool:
        parsed = urlparse(url)
        return parsed.scheme in ("http", "https") and bool(parsed.netloc)

    def generate_qr(self):
        raw_url = self.link_entry.get()
        url = self.normalize_url(raw_url)

        if not url:
            messagebox.showwarning("Aviso", "Digite um link para gerar o QR Code.")
            return

        if not self.is_valid_url(url):
            messagebox.showerror("Erro", "Digite um link válido. Ex: https://seusite.com")
            return

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)

        self.qr_pil_image = qr.make_image(fill_color="black", back_color="white").convert("RGB")
        preview = self.qr_pil_image.resize((280, 280))
        self.qr_image = ImageTk.PhotoImage(preview)

        self.image_label.config(image=self.qr_image)
        self.result_label.config(text=url)

    def save_qr(self):
        if self.qr_pil_image is None:
            messagebox.showwarning("Aviso", "Gere um QR Code antes de salvar.")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG Files", "*.png")],
            title="Salvar QR Code"
        )

        if file_path:
            self.qr_pil_image.save(file_path)
            messagebox.showinfo("Sucesso", "QR Code salvo com sucesso.")

    def clear_all(self):
        self.link_entry.delete(0, "end")
        self.image_label.config(image="")
        self.result_label.config(text="")
        self.qr_image = None
        self.qr_pil_image = None


if __name__ == "__main__":
    root = Tk()
    app = QRCodeApp(root)
    root.mainloop()
