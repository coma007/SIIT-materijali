package types.log;

public class Stack {

	public String file;;
	public int line;
	public String code;

	public String getFile() {
		return file;
	}

	public void setFile(String file) {
		this.file = file;
	}

	public int getLine() {
		return line;
	}

	public void setLine(int line) {
		this.line = line;
	}

	public String getCode() {
		return code;
	}

	public void setCode(String code) {
		this.code = code;
	}

	@Override
	public String toString() {
		return "Stack [file=" + file + ", line=" + line + ", code=" + code + "]";
	}

}
