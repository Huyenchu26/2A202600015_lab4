import sys
sys.stdout.reconfigure(encoding='utf-8')

from tools import search_flights, search_hotels, calculate_budget

def main():
    with open('test_tools_output.txt', 'w', encoding='utf-8') as f:
        # Redirect print to file
        sys.stdout = f
        print("="*50)
        print(" TEST: search_flights")
        print("="*50)
        print("\n[Trường hợp 1] Xuôi chiều: Hà Nội -> Đà Nẵng")
        print(search_flights.invoke({"origin": "Hà Nội", "destination": "Đà Nẵng"}))
        
        print("\n[Trường hợp 2] Ngược chiều: Đà Nẵng -> Hà Nội")
        print(search_flights.invoke({"origin": "Đà Nẵng", "destination": "Hà Nội"}))
        
        print("\n[Trường hợp 3] Không có tuyến bay: Hà Nội -> New York")
        print(search_flights.invoke({"origin": "Hà Nội", "destination": "New York"}))
        
        print("\n" + "="*50)
        print(" TEST: search_hotels")
        print("="*50)
        print("\n[Trường hợp 1] Tại Đà Nẵng với max giá 1_000_000đ/đêm")
        print(search_hotels.invoke({"city": "Đà Nẵng", "max_price_per_night": 1_000_000}))
        
        print("\n[Trường hợp 2] Không có khách sạn: Đà Nẵng với max giá 1_000đ/đêm")
        print(search_hotels.invoke({"city": "Đà Nẵng", "max_price_per_night": 1_000}))
        
        print("\n" + "="*50)
        print(" TEST: calculate_budget")
        print("="*50)
        print("\n[Trường hợp 1] Đủ ngân sách: Ngân sách 5_000_000đ, chi phí 2_650_000đ")
        print(calculate_budget.invoke({"total_budget": 5_000_000, "expenses": "vé_máy_bay:1450000,khách_sạn:1200000"}))
        
        print("\n[Trường hợp 2] Vượt ngân sách: Ngân sách 2_000_000đ, chi phí 2_650_000đ")
        print(calculate_budget.invoke({"total_budget": 2_000_000, "expenses": "vé_máy_bay:1450000,khách_sạn:1200000"}))
        
        print("\n[Trường hợp 3] Lỗi định dạng")
        print(calculate_budget.invoke({"total_budget": 5_000_000, "expenses": "vé_máy_bay-1450000"}))

if __name__ == "__main__":
    main()
