import random
import time
from main import is_prime, power, find_primitive_root, generate_prime


def simulate_message_exchange(alice_key, bob_key, eve_alice_key, eve_bob_key):
    """
    Mô phỏng việc trao đổi tin nhắn giữa Alice và Bob với sự can thiệp của Eve.

    Tham số:
        alice_key: Khóa bí mật chung mà Alice nghĩ rằng cô ấy chia sẻ với Bob
        bob_key: Khóa bí mật chung mà Bob nghĩ rằng anh ấy chia sẻ với Alice
        eve_alice_key: Khóa bí mật chung giữa Eve và Alice
        eve_bob_key: Khóa bí mật chung giữa Eve và Bob
    """
    print("\n=== MÔ PHỎNG TRAO ĐỔI TIN NHẮN QUA TERMINAL ===")

    # Mô phỏng tin nhắn từ Alice đến Bob
    print("\n[Terminal của Alice]")
    message = input("Alice nhập tin nhắn gửi cho Bob: ")

    # Mã hóa đơn giản bằng cách XOR với khóa (chỉ để minh họa)
    encrypted_for_bob = ''.join(
        chr(ord(c) ^ (alice_key % 255)) for c in message)
    print(f"Alice mã hóa tin nhắn bằng khóa {alice_key} và gửi đi...")

    # Eve chặn tin nhắn
    print("\n[Eve chặn tin nhắn]")
    time.sleep(1)
    print("Eve đã chặn tin nhắn từ Alice!")

    # Eve giải mã tin nhắn bằng khóa chung với Alice
    decrypted_by_eve = ''.join(chr(ord(c) ^ (eve_alice_key % 255))
                               for c in encrypted_for_bob)
    print(
        f"Eve giải mã tin nhắn bằng khóa {eve_alice_key}: \"{decrypted_by_eve}\"")

    # Eve có thể sửa đổi tin nhắn
    modified_message = decrypted_by_eve
    should_modify = input(
        "Eve có muốn sửa đổi tin nhắn không? (y/n): ").lower() == 'y'

    if should_modify:
        modified_message = input("Eve nhập tin nhắn mới: ")
        print(f"Eve đã sửa đổi tin nhắn thành: \"{modified_message}\"")

    # Eve mã hóa lại tin nhắn bằng khóa chung với Bob
    re_encrypted_for_bob = ''.join(
        chr(ord(c) ^ (eve_bob_key % 255)) for c in modified_message)
    print("Eve mã hóa lại tin nhắn và chuyển tiếp cho Bob...")

    # Bob nhận và giải mã tin nhắn
    print("\n[Terminal của Bob]")
    time.sleep(1)
    decrypted_by_bob = ''.join(chr(ord(c) ^ (bob_key % 255))
                               for c in re_encrypted_for_bob)
    print(f"Bob nhận tin nhắn và giải mã bằng khóa {bob_key}")
    print(f"Bob đọc tin nhắn: \"{decrypted_by_bob}\"")

    # Bob trả lời
    print("\n[Bob trả lời]")
    reply = input("Bob nhập tin nhắn trả lời cho Alice: ")

    # Mã hóa tin nhắn trả lời
    encrypted_for_alice = ''.join(chr(ord(c) ^ (bob_key % 255)) for c in reply)
    print(f"Bob mã hóa tin nhắn bằng khóa {bob_key} và gửi đi...")

    # Eve chặn tin nhắn trả lời
    print("\n[Eve chặn tin nhắn trả lời]")
    time.sleep(1)
    print("Eve đã chặn tin nhắn từ Bob!")

    # Eve giải mã tin nhắn trả lời
    decrypted_reply_by_eve = ''.join(
        chr(ord(c) ^ (eve_bob_key % 255)) for c in encrypted_for_alice)
    print(
        f"Eve giải mã tin nhắn bằng khóa {eve_bob_key}: \"{decrypted_reply_by_eve}\"")

    # Eve có thể sửa đổi tin nhắn trả lời
    modified_reply = decrypted_reply_by_eve
    should_modify_reply = input(
        "Eve có muốn sửa đổi tin nhắn trả lời không? (y/n): ").lower() == 'y'

    if should_modify_reply:
        modified_reply = input("Eve nhập tin nhắn trả lời mới: ")
        print(f"Eve đã sửa đổi tin nhắn trả lời thành: \"{modified_reply}\"")

    # Eve mã hóa lại tin nhắn trả lời
    re_encrypted_for_alice = ''.join(
        chr(ord(c) ^ (eve_alice_key % 255)) for c in modified_reply)
    print("Eve mã hóa lại tin nhắn và chuyển tiếp cho Alice...")

    # Alice nhận và giải mã tin nhắn trả lời
    print("\n[Terminal của Alice]")
    time.sleep(1)
    decrypted_reply_by_alice = ''.join(
        chr(ord(c) ^ (alice_key % 255)) for c in re_encrypted_for_alice)
    print(f"Alice nhận tin nhắn và giải mã bằng khóa {alice_key}")
    print(f"Alice đọc tin nhắn: \"{decrypted_reply_by_alice}\"")

    print("\n=== KẾT THÚC MÔ PHỎNG ===")
    print("Như bạn có thể thấy, Eve có thể đọc và sửa đổi tất cả tin nhắn mà Alice và Bob không hề biết!")


def diffie_hellman_mitm_attack():
    """
    Minh họa tấn công Man-in-the-Middle (MITM) trong giao thức trao đổi khóa Diffie-Hellman.

    Trong tấn công này, kẻ tấn công (Eve) chặn giao tiếp giữa Alice và Bob:
    1. Alice và Bob thống nhất các tham số công khai p và g
    2. Alice gửi khóa công khai A cho Bob, nhưng Eve chặn lại
    3. Eve tạo khóa bí mật riêng e và gửi khóa công khai E cho Bob (giả mạo là từ Alice)
    4. Bob gửi khóa công khai B cho Alice, nhưng Eve cũng chặn lại
    5. Eve gửi khóa công khai E cho Alice (giả mạo là từ Bob)
    6. Alice và Bob thiết lập các khóa bí mật chung khác nhau, cả hai đều với Eve
    7. Eve có thể giải mã, đọc, thậm chí sửa đổi thông điệp trước khi mã hóa lại và chuyển tiếp

    Đây là lý do tại sao xác thực là cần thiết trong giao thức Diffie-Hellman.
    """
    # 1. Thống nhất một số nguyên tố công khai (p) và một căn nguyên thủy (g)
    p = generate_prime(100, 500)
    g = find_primitive_root(p)

    if g is None:
        print(f"Không thể tìm thấy căn nguyên thủy cho {p}. Hủy bỏ.")
        return

    print("=== THIẾT LẬP THAM SỐ CÔNG KHAI ===")
    print(f"Số nguyên tố đã thống nhất công khai (p): {p}")
    print(f"Căn nguyên thủy đã thống nhất công khai (g): {g}")
    print()

    # 2. Khóa bí mật và công khai của Alice
    alice_secret = random.randint(1, p - 1)
    alice_public = power(g, alice_secret, p)
    print("=== ALICE ===")
    print(f"Khóa bí mật của Alice (a): {alice_secret}")
    print(f"Khóa công khai của Alice (A = g^a mod p): {alice_public}")
    print()

    # 3. Khóa bí mật và công khai của Bob
    bob_secret = random.randint(1, p - 1)
    bob_public = power(g, bob_secret, p)
    print("=== BOB ===")
    print(f"Khóa bí mật của Bob (b): {bob_secret}")
    print(f"Khóa công khai của Bob (B = g^b mod p): {bob_public}")
    print()

    # 4. Eve tạo khóa bí mật riêng của mình
    eve_secret = random.randint(1, p - 1)
    eve_public = power(g, eve_secret, p)
    print("=== EVE (KẺ TẤN CÔNG) ===")
    print(f"Khóa bí mật của Eve (e): {eve_secret}")
    print(f"Khóa công khai của Eve (E = g^e mod p): {eve_public}")
    print()

    # 5. Tấn công MITM: Eve chặn khóa công khai của Alice và Bob
    print("=== TIẾN HÀNH TẤN CÔNG MAN-IN-THE-MIDDLE ===")
    print("1. Alice gửi A cho Bob, nhưng Eve chặn lại")
    print("2. Eve gửi E cho Bob (giả mạo là từ Alice)")
    print("3. Bob gửi B cho Alice, nhưng Eve chặn lại")
    print("4. Eve gửi E cho Alice (giả mạo là từ Bob)")
    print()

    # 6. Alice tính toán khóa bí mật chung với Eve (nghĩ rằng đó là Bob)
    alice_eve_secret = power(eve_public, alice_secret, p)
    print("=== KẾT QUẢ TRAO ĐỔI KHÓA ===")
    print(
        f"Alice tính toán khóa bí mật: {alice_eve_secret} (sử dụng E^a mod p)")

    # 7. Bob tính toán khóa bí mật chung với Eve (nghĩ rằng đó là Alice)
    bob_eve_secret = power(eve_public, bob_secret, p)
    print(f"Bob tính toán khóa bí mật: {bob_eve_secret} (sử dụng E^b mod p)")

    # 8. Eve tính toán khóa bí mật chung với Alice và Bob
    eve_alice_secret = power(alice_public, eve_secret, p)
    eve_bob_secret = power(bob_public, eve_secret, p)
    print(
        f"Eve tính toán khóa bí mật với Alice: {eve_alice_secret} (sử dụng A^e mod p)")
    print(
        f"Eve tính toán khóa bí mật với Bob: {eve_bob_secret} (sử dụng B^e mod p)")
    print()

    # 9. Xác minh rằng Eve có thể giải mã và mã hóa lại thông điệp
    print("=== PHÂN TÍCH TẤN CÔNG ===")
    print(
        f"Alice nghĩ rằng cô ấy đang chia sẻ khóa bí mật {alice_eve_secret} với Bob")
    print(
        f"Bob nghĩ rằng anh ấy đang chia sẻ khóa bí mật {bob_eve_secret} với Alice")
    print(
        f"Eve biết khóa bí mật {eve_alice_secret} để giải mã thông điệp từ Alice")
    print(
        f"Eve biết khóa bí mật {eve_bob_secret} để giải mã thông điệp từ Bob")
    print()

    print("=== KẾT LUẬN ===")
    print("Eve có thể:")
    print("1. Đọc tất cả thông điệp được trao đổi giữa Alice và Bob")
    print("2. Sửa đổi thông điệp trước khi chuyển tiếp")
    print("3. Giả mạo thông điệp hoàn toàn mới")
    print()
    print("Đây là lý do tại sao xác thực (như chữ ký số) là cần thiết khi sử dụng Diffie-Hellman")

    # 10. Mô phỏng trao đổi tin nhắn qua terminal
    simulate = input(
        "\nBạn có muốn mô phỏng trao đổi tin nhắn qua terminal không? (y/n): ").lower() == 'y'
    if simulate:
        simulate_message_exchange(
            alice_eve_secret, bob_eve_secret, eve_alice_secret, eve_bob_secret)


if __name__ == "__main__":
    diffie_hellman_mitm_attack()
