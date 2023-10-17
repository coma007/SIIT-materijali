package rs.ac.uns.ftn.informatika.jpa.mapper;

import org.modelmapper.ModelMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import rs.ac.uns.ftn.informatika.jpa.dto.TeacherDTO;
import rs.ac.uns.ftn.informatika.jpa.model.Teacher;

@Component
public class TeacherDTOMapper {
	
	private static ModelMapper modelMapper;
	
	@Autowired
	public TeacherDTOMapper(ModelMapper modelMapper) {
		this.modelMapper = modelMapper;
	}

	public static Teacher fromDTOtoTeacher(TeacherDTO dto) {
		return modelMapper.map(dto, Teacher.class);
	}
	
	public static TeacherDTO fromTeachertoDTO(Teacher dto) {
		return modelMapper.map(dto, TeacherDTO.class);
	}
}
