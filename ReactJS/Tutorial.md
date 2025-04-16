# React App
* React ecosystem
* Component:
    - Là 1 hàm hoặc 1 lớp trong React trả vê UI
    - Mỗi component làm 1 nv cụ thể (button, form,...)
* Building Components:
    - Building components
    - Rendering markup with JSX
    - Managing state
    - Passing input via props
    - Debbuging
* State (Object)
    - là một đối tương (giá trị) chứa dữ liệu nội bộ trong component, có thể thay đổi trong suốt vòng đời của component
    - Đặc điểm:
        + Động: State có thể được cập nhật thông qua các hành động của người dùng (click, nhập liệu) hoặc API
        + Nội bộ: thuộc component, không được truyền ra ngoài như props
        + Kích hoạt re-render: Khi state thay đổi, React tự động họi lại hàm render (hoặc hàm của Function Component) để cập nhật lại giao diện
* props (Properties)
    - Truyền dữ liệu (readonly) từ component cha xuống component con
- mu·tate -> change
- mu·ta·ble -> changeable
- im·mu·ta·ble -> unchangeable