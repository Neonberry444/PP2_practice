import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Paint: R-Red, G-Green, B-Blue, Y-Yellow | C-Circle, S-Square, E-Eraser")
    clock = pygame.time.Clock()
    
    radius = 15
    # Possible shapes: 'circle', 'rectangle'
    shape = 'circle'
    # Current color selection
    color_mode = (0, 0, 255) # Start with Blue
    
    # points will now store dictionaries: {'pos': (x,y), 'color': (r,g,b), 'shape': 'type', 'radius': r}
    points = []
    
    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                # Exit functionality
                if event.key == pygame.K_w and ctrl_held: return
                if event.key == pygame.K_F4 and alt_held: return
                if event.key == pygame.K_ESCAPE: return
            
                # --- Color Selection ---
                if event.key == pygame.K_r:
                    color_mode = (255, 0, 0) # Red
                elif event.key == pygame.K_g:
                    color_mode = (0, 255, 0) # Green
                elif event.key == pygame.K_b:
                    color_mode = (0, 0, 255) # Blue
                elif event.key == pygame.K_y:
                    color_mode = (255, 255, 0) # Yellow
                
                # --- Shape Selection ---
                if event.key == pygame.K_c:
                    shape = 'circle'
                elif event.key == pygame.K_s:
                    shape = 'rectangle'
                
                # --- Eraser ---
                # Simply sets the color to the background color (Black)
                elif event.key == pygame.K_e:
                    color_mode = (0, 0, 0) 

            # Radius adjustment via Mouse Wheel or Buttons
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # Left click grows
                    radius = min(200, radius + 1)
                elif event.button == 3: # Right click shrinks
                    radius = max(1, radius - 1)
            
            # Draw logic: If mouse is moving and button is held
            if event.type == pygame.MOUSEMOTION:
                if event.buttons[0]: # If left mouse button is held down
                    position = event.pos
                    # Add current state to points list
                    new_point = {
                        'pos': position,
                        'color': color_mode,
                        'shape': shape,
                        'radius': radius
                    }
                    points.append(new_point)
                    # Limit buffer to prevent lag
                    points = points[-512:]
                
        screen.fill((0, 0, 0))
        
        # Draw every point stored in the list
        for p in points:
            drawShape(screen, p)
        
        pygame.display.flip()
        clock.tick(60)

def drawShape(screen, point_data):
    """Determines which shape to draw based on point data."""
    pos = point_data['pos']
    color = point_data['color']
    r = point_data['radius']
    
    if point_data['shape'] == 'circle':
        pygame.draw.circle(screen, color, pos, r)
    elif point_data['shape'] == 'rectangle':
        # Drawing from center: adjust top-left based on radius
        pygame.draw.rect(screen, color, (pos[0] - r, pos[1] - r, r * 2, r * 2))

main()